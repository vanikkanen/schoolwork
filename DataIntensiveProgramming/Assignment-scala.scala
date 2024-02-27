// Databricks notebook source
// MAGIC %md
// MAGIC # Data-Intensive Programming - Assignment
// MAGIC
// MAGIC This is the **Scala** version of the assignment. Switch to the Python version, if you want to do the assignment in Python.
// MAGIC
// MAGIC In all tasks, add your solutions to the cells following the task instructions. You are free to add new cells if you want.
// MAGIC
// MAGIC Don't forget to **submit your solutions to Moodle** once your group is finished with the assignment.
// MAGIC
// MAGIC ## Basic tasks (compulsory)
// MAGIC
// MAGIC There are in total seven basic tasks that every group must implement in order to have an accepted assignment.
// MAGIC
// MAGIC The basic task 1 is a warming up task and it deals with some video game sales data. The task asks you to do some basic aggregation operations with Spark data frames.
// MAGIC
// MAGIC The other basic tasks (basic tasks 2-7) are all related and deal with data from [https://moneypuck.com/data.htm](https://moneypuck.com/data.htm) that contains information about every shot in all National Hockey League ([NHL](https://en.wikipedia.org/wiki/National_Hockey_League), [ice hockey](https://en.wikipedia.org/wiki/Ice_hockey)) matches starting from season 2011-12 and ending with the last completed season, 2022-23. The tasks ask you to calculate the results of the matches based on the given data as well as do some further calculations. Knowledge about ice hockey or NHL is not required, and the task instructions should be sufficient in order to gain enough context for the tasks.
// MAGIC
// MAGIC ## Additional tasks (optional, can provide course points)
// MAGIC
// MAGIC There are in total of three additional tasks that can be done to gain some course points.
// MAGIC
// MAGIC The first additional task asks you to do all the basic tasks in an optimized way. It is possible that you can some points from this without directly trying by just implementing the basic tasks in an efficient manner.
// MAGIC
// MAGIC The other two additional tasks are separate tasks and do not relate to any other basic or additional tasks. One of them asks you to load in unstructured text data and do some calculations based on the words found from the data. The other asks you to utilize the K-Means algorithm to partition the given building data.
// MAGIC
// MAGIC It is possible to gain partial points from the additional tasks. I.e., if you have not completed the task fully but have implemented some part of the task, you might gain some appropriate portion of the points from the task.
// MAGIC

// COMMAND ----------

// import statements for the entire notebook
// add anything that is required here

import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.types.{StructType, StructField}

import org.apache.spark.ml.clustering.KMeans
import org.apache.spark.ml.feature.VectorAssembler
import scala.util.control.Breaks._

// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 1 - Sales data
// MAGIC
// MAGIC The CSV file `assignment/sales/video_game_sales.csv` in the [Shared container](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2Fe0c78478-e7f8-429c-a25f-015eae9f54bb%2FresourceGroups%2Ftuni-cs320-f2023-rg%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftunics320f2023gen2/path/shared/etag/%220x8DBB0695B02FFFE%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None) contains video game sales data (from [https://www.kaggle.com/datasets/ashaheedq/video-games-sales-2019/data](https://www.kaggle.com/datasets/ashaheedq/video-games-sales-2019/data)). The direct address for the dataset is: `abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/sales/video_game_sales.csv`
// MAGIC
// MAGIC Load the data from the CSV file into a data frame. The column headers and the first few data lines should give sufficient information about the source dataset.
// MAGIC
// MAGIC Only data for sales in the first ten years of the 21st century should be considered in this task, i.e. years 2000-2009.
// MAGIC
// MAGIC Using the data, find answers to the following:
// MAGIC
// MAGIC - Which publisher had the highest total sales in video games in European Union in years 2000-2009?
// MAGIC - What were the total yearly sales, in European Union and globally, for this publisher in year 2000-2009
// MAGIC

// COMMAND ----------

// Create schema for the DataFrame
val schema = StructType(
      Seq(
        StructField("Rank", IntegerType, nullable = true),
        StructField("Name", StringType, nullable = true),
        StructField("Platform", StringType, nullable = true),
        StructField("Year", IntegerType, nullable = true),
        StructField("Genre", StringType, nullable = true),
        StructField("Publisher", StringType, nullable = true),
        StructField("NA_Sales", DoubleType, nullable = true),
        StructField("EU_Sales", DoubleType, nullable = true),
        StructField("JP_Sales", DoubleType, nullable = true),
        StructField("Other_Sales", DoubleType, nullable = true),
        StructField("Global_Sales", DoubleType, nullable = true)
      )
    )

val rawEUPublisherDF: DataFrame = spark.read
.option("header", "true") // Header row
.option("delimiter", ",")
.schema(schema) // We give the correct schema so spark doesnt have to figure it out
.csv("abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/sales/video_game_sales.csv")

// Dropping unnecessary columns
val EUPublisherDF: DataFrame = rawEUPublisherDF.drop("Rank","Name","Platform","Genre","NA_Sales","JP_Sales","Other_Sales")

val filteredDF: DataFrame = EUPublisherDF
  .filter(col("Year").between(2000, 2009))

val bestEUPublisherRow = filteredDF
  .groupBy("Publisher")
  .agg(sum("EU_Sales").as("Total_EU_Sales"))
  .orderBy(desc("Total_EU_Sales")).first()


val bestEUPublisher: String = bestEUPublisherRow.getAs[String]("Publisher") // Which publisher had the highest total sales in video games in European Union in years 2000-2009?

val bestEUPublisherSales: DataFrame = filteredDF // What were the total yearly sales, in European Union and globally, for this publisher in year 2000-2009?
.filter(col("Publisher") === bestEUPublisher) // Get the data about the correct publisher
.groupBy("Year") // Data by year
.agg(sum("EU_Sales").as("Total_EU_Sales"), sum("Global_Sales").as("Total_Global_Sales")) // Calculate the total sales by year
.orderBy(asc("Year")) // Order for presentation
.withColumn("Total_EU_Sales", round(col("Total_EU_Sales"), 3)) // Round for presentation
.withColumn("Total_Global_Sales", round(col("Total_Global_Sales"), 3))

println(s"The publisher with the highest total video game sales in European Union is: '${bestEUPublisher}'")
println("Sales data for the publisher:")
bestEUPublisherSales.show(10)


// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 2 - Shot data from NHL matches
// MAGIC
// MAGIC A parquet file in the [Shared container](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2Fe0c78478-e7f8-429c-a25f-015eae9f54bb%2FresourceGroups%2Ftuni-cs320-f2023-rg%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftunics320f2023gen2/path/shared/etag/%220x8DBB0695B02FFFE%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None) at folder `assignment/nhl_shots.parquet` from [https://moneypuck.com/data.htm](https://moneypuck.com/data.htm) contains information about every shot in all National Hockey League ([NHL](https://en.wikipedia.org/wiki/National_Hockey_League), [ice hockey](https://en.wikipedia.org/wiki/Ice_hockey)) matches starting from season 2011-12 and ending with the last completed season, 2022-23.
// MAGIC
// MAGIC In this task you should load the data with all of the rows into a data frame. This data frame object will then be used in the following basic tasks 3-7.
// MAGIC
// MAGIC ### Background information
// MAGIC
// MAGIC Each NHL season is divided into regular season and playoff season. In the regular season the teams play up to 82 games with the best teams continuing to the playoff season. During the playoff season the remaining teams are paired and each pair play best-of-seven series of games to determine which team will advance to the next phase.
// MAGIC
// MAGIC In ice hockey each game has a home team and an away team. The regular length of a game is three 20 minute periods, i.e. 60 minutes or 3600 seconds. The team that scores more goals in the regulation time is the winner of the game.
// MAGIC
// MAGIC If the scoreline is even after this regulation time:
// MAGIC
// MAGIC - In playoff games, the game will be continued until one of the teams score a goal with the scoring team being the winner.
// MAGIC - In regular season games, there is an extra time that can last a maximum of 5 minutes (300 seconds). If one of the teams score, the game ends with the scoring team being the winner. If there is no goals in the extra time, there would be a shootout competition to determine the winner. These shootout competitions are not considered in this assignment, and the shots from those are not included in the raw data.
// MAGIC
// MAGIC **Columns in the data**
// MAGIC
// MAGIC Each row in the given data represents one shot in a game.
// MAGIC
// MAGIC The column description from the source website. Not all of these will be needed in this assignment.
// MAGIC
// MAGIC | column name | column type | description |
// MAGIC | ----------- | ----------- | ----------- |
// MAGIC | shotID      | integer | Unique id for each shot |
// MAGIC | homeTeamCode | string | The home team in the game. For example: TOR, MTL, NYR, etc. |
// MAGIC | awayTeamCode | string | The away team in the game |
// MAGIC | season | integer | Season the shot took place in. Example: 2009 for the 2009-2010 season |
// MAGIC | isPlayOffGame | integer | Set to 1 if a playoff game, otherwise 0 |
// MAGIC | game_id | integer | The NHL Game_id of the game the shot took place in |
// MAGIC | time | integer | Seconds into the game of the shot |
// MAGIC | period | integer | Period of the game |
// MAGIC | team | string | The team taking the shot. HOME or AWAY |
// MAGIC | location | string | The zone the shot took place in. HOMEZONE, AWAYZONE, or Neu. Zone |
// MAGIC | event | string | Whether the shot was a shot on goal (SHOT), goal, (GOAL), or missed the net (MISS) |
// MAGIC | homeTeamGoals | integer | Home team goals before the shot took place |
// MAGIC | awayTeamGoals | integer | Away team goals before the shot took place |
// MAGIC | homeTeamWon | integer | Set to 1 if the home team won the game. Otherwise 0. |
// MAGIC | shotType | string | Type of the shot. (Slap, Wrist, etc) |
// MAGIC

// COMMAND ----------

val rawShotsDF: DataFrame = spark.read.parquet("abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/nhl_shots.parquet")
// Filter away the useless columns not used later
val shotsDF: DataFrame = rawShotsDF.drop("shotType","location","homeTeamWon", "awayTeamGoals", "homeTeamGoals","period")

//shotsDF.show(10)

// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 3 - Game data frame
// MAGIC
// MAGIC Create a match data frame for all the game included in the shots data frame created in basic task 2.
// MAGIC
// MAGIC The output should contain one row for each game.
// MAGIC
// MAGIC The following columns should be included in the final data frame for this task:
// MAGIC
// MAGIC | column name    | column type | description |
// MAGIC | -------------- | ----------- | ----------- |
// MAGIC | season         | integer     | Season the game took place in. Example: 2009 for the 2009-2010 season |
// MAGIC | game_id        | integer     | The NHL Game_id of the game |
// MAGIC | homeTeamCode   | string      | The home team in the game. For example: TOR, MTL, NYR, etc. |
// MAGIC | awayTeamCode   | string      | The away team in the game |
// MAGIC | isPlayOffGame  | integer     | Set to 1 if a playoff game, otherwise 0 |
// MAGIC | homeTeamGoals  | integer     | Number of goals scored by the home team |
// MAGIC | awayTeamGoals  | integer     | Number of goals scored by the away team |
// MAGIC | lastGoalTime   | integer     | The time in seconds for the last goal in the game. 0 if there was no goals in the game. |
// MAGIC
// MAGIC All games had at least some shots but there are some games that did not have any goals either in the regulation 60 minutes or in the extra time.
// MAGIC
// MAGIC Note, that for a couple of games there might be some shots, including goal-scoring ones, that are missing from the original dataset. For example, there might be a game with a final scoreline of 3-4 but only 6 of the goal-scoring shots are included in the dataset. Your solution does not have to try to take these rare occasions of missing data into account. I.e., you can do all the tasks with the assumption that there are no missing or invalid data.
// MAGIC

// COMMAND ----------

val gamesDF: DataFrame = shotsDF
  .groupBy("season", "game_id", "homeTeamCode", "awayTeamCode", "isPlayOffGame")
  .agg(
    sum(when(col("team") === "HOME" && col("event") === "GOAL", 1).otherwise(0)).alias("homeTeamGoals"),
    sum(when(col("team") === "AWAY" && col("event") === "GOAL", 1).otherwise(0)).alias("awayTeamGoals"),
     when(max(when(col("event") === "GOAL", col("time"))).isNull, 0).otherwise(max(when(col("event") === "GOAL", col("time")))).alias("lastGoalTime")
  )

println(s"Number of games in the DataFrame: '${gamesDF.count()}'")
gamesDF.show(10)
/*
val specificRow = gamesDF.filter("game_id = 30236 AND season = 2013")
specificRow.show()
*/


// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 4 - Game wins during playoff seasons
// MAGIC
// MAGIC Create a data frame that uses the game data frame from the basic task 3 and contains aggregated number of wins and losses for each team and for each playoff season, i.e. for games which have been marked as playoff games. Only teams that have played in at least one playoff game in the considered season should be included in the final data frame.
// MAGIC
// MAGIC The following columns should be included in the final data frame:
// MAGIC
// MAGIC | column name    | column type | description |
// MAGIC | -------------- | ----------- | ----------- |
// MAGIC | season         | integer     | The season for the data. Example: 2009 for the 2009-2010 season |
// MAGIC | teamCode       | string      | The code for the team. For example: TOR, MTL, NYR, etc. |
// MAGIC | games          | integer     | Number of playoff games the team played in the given season |
// MAGIC | wins           | integer     | Number of wins in playoff games the team had in the given season |
// MAGIC | losses         | integer     | Number of losses in playoff games the team had in the given season |
// MAGIC
// MAGIC Playoff games where a team scored more goals than their opponent are considered winning games. And playoff games where a team scored less goals than the opponent are considered losing games.
// MAGIC
// MAGIC In real life there should not be any playoff games where the final score line was even but due to some missing shot data you might end up with a couple of playoff games that seems to have ended up in a draw. These possible "drawn" playoff games can be left out from the win/loss calculations.
// MAGIC

// COMMAND ----------

val playoffGamesDF: DataFrame = gamesDF.filter("isPlayoffGame = 1") // Get only the playoffs

// Get the winning and losing home games for each of the teams in the playoffs
val winLossHomeDF = playoffGamesDF.groupBy("season", "homeTeamCode").agg(
  sum(when(col("homeTeamGoals") > col("awayTeamGoals"), 1).otherwise(0)).alias("wins"),
  sum(when(col("homeTeamGoals") < col("awayTeamGoals"), 1).otherwise(0)).alias("losses"),
  count("*").alias("games")
)
/*
println(s"Number of games in the DataFrame: '${winLossHomeDF.count()}'")
winLossHomeDF.show()
*/

// Get the winning and losing away games for each of the teams in the playoffs
val winLossAwayDF = playoffGamesDF.groupBy("season", "awayTeamCode").agg(
  sum(when(col("awayTeamGoals") > col("homeTeamGoals"), 1).otherwise(0)).alias("wins"),
  sum(when(col("awayTeamGoals") < col("homeTeamGoals"), 1).otherwise(0)).alias("losses"),
  count("*").alias("games")
)
/*
println(s"Number of games in the DataFrame: '${winLossAwayDF.count()}'")
winLossAwayDF.show()
*/

// Combine the two DataFrames using union
val combinedDF = winLossHomeDF
  .select("season", "homeTeamCode", "games", "wins", "losses")
  .union(
    winLossAwayDF
      .select("season", "awayTeamCode", "games", "wins", "losses")
      .withColumnRenamed("awayTeamCode", "homeTeamCode") // So the dataFrames are easier to unionize
  )

// Group by 'season' and 'teamCode', and aggregate
val aggregatedPlayoffDF = combinedDF.groupBy("season", "homeTeamCode")
  .agg(
    sum("games").alias("games"),
    sum("wins").alias("wins"),
    sum("losses").alias("losses")
  )

// Rename 'homeTeamCode' to 'teamCode'
val playoffDF = aggregatedPlayoffDF.withColumnRenamed("homeTeamCode", "teamCode") 


println(s"Number of games in the DataFrame: '${playoffDF.count()}'")
playoffDF.show()


// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 5 - Best playoff teams
// MAGIC
// MAGIC Using the playoff data frame created in basic task 4 create a data frame containing the win-loss record for best playoff team, i.e. the team with the most wins, for each season. You can assume that there are no ties for the highest amount of wins in each season.
// MAGIC
// MAGIC The following columns should be included in the final data frame:
// MAGIC
// MAGIC | column name    | column type | description |
// MAGIC | -------------- | ----------- | ----------- |
// MAGIC | season         | integer     | The season for the data. Example: 2009 for the 2009-2010 season |
// MAGIC | teamCode       | string      | The team code for the best performing playoff team in the given season. For example: TOR, MTL, NYR, etc. |
// MAGIC | games          | integer     | Number of playoff games the best performing playoff team played in the given season |
// MAGIC | wins           | integer     | Number of wins in playoff games the best performing playoff team had in the given season |
// MAGIC | losses         | integer     | Number of losses in playoff games the best performing playoff team had in the given season |
// MAGIC
// MAGIC Finally, fetch the details for the best playoff team in season 2022.
// MAGIC

// COMMAND ----------

// Window partition by season and order by wins in descending order
val windowSpec = Window.partitionBy("season").orderBy(col("wins").desc)

// Create a new column "rank" based on the window specification
val rankedDF = playoffDF.withColumn("rank", rank().over(windowSpec))

// Filter for the top-ranked team in each season
val bestTeamDF = rankedDF.filter("rank = 1")


val bestPlayoffTeams: DataFrame = bestTeamDF.select(
  col("season"),
  col("teamCode"),
  col("games"),
  col("wins"),
  col("losses")
)

bestPlayoffTeams.show()


// COMMAND ----------

val bestPlayoffTeam2022: Row = bestPlayoffTeams.filter("season = 2022").first()

println("Best playoff team in 2022:")
println(s"    Team: ${bestPlayoffTeam2022.getAs[String]("teamCode")}")
println(s"    Games: ${bestPlayoffTeam2022.getAs[Long]("games")}")
println(s"    Wins: ${bestPlayoffTeam2022.getAs[Long]("wins")}")
println(s"    Losses: ${bestPlayoffTeam2022.getAs[Long]("losses")}")
println("=========================================================")


// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 6 - Regular season points
// MAGIC
// MAGIC Create a data frame that uses the game data frame from the basic task 3 and contains aggregated data for each team and for each season for the regular season matches, i.e. the non-playoff matches.
// MAGIC
// MAGIC The following columns should be included in the final data frame:
// MAGIC
// MAGIC | column name    | column type | description |
// MAGIC | -------------- | ----------- | ----------- |
// MAGIC | season         | integer     | The season for the data. Example: 2009 for the 2009-2010 season |
// MAGIC | teamCode       | string      | The code for the team. For example: TOR, MTL, NYR, etc. |
// MAGIC | games          | integer     | Number of non-playoff games the team played in the given season |
// MAGIC | wins           | integer     | Number of wins in non-playoff games the team had in the given season |
// MAGIC | losses         | integer     | Number of losses in non-playoff games the team had in the given season |
// MAGIC | goalsScored    | integer     | Total number goals scored by the team in non-playoff games in the given season |
// MAGIC | goalsConceded  | integer     | Total number goals scored against the team in non-playoff games in the given season |
// MAGIC | points         | integer     | Total number of points gathered by the team in non-playoff games in the given season |
// MAGIC
// MAGIC Points from each match are received as follows (in the context of this assignment, these do not exactly match the NHL rules):
// MAGIC
// MAGIC | points | situation |
// MAGIC | ------ | --------- |
// MAGIC | 3      | team scored more goals than the opponent during the regular 60 minutes |
// MAGIC | 2      | the score line was even after 60 minutes but the team scored a winning goal during the extra time |
// MAGIC | 1      | the score line was even after 60 minutes but the opponent scored a winning goal during the extra time or there were no goals in the extra time |
// MAGIC | 0      | the opponent scored more goals than the team during the regular 60 minutes |
// MAGIC
// MAGIC In the regular season the following table shows how wins and losses should be considered (in the context of this assignment):
// MAGIC
// MAGIC | win | loss | situation |
// MAGIC | --- | ---- | --------- |
// MAGIC | Yes | No   | team gained at least 2 points from the match |
// MAGIC | No  | Yes  | team gain at most 1 point from the match |
// MAGIC

// COMMAND ----------

val regularGamesDF: DataFrame = gamesDF.filter("isPlayoffGame = 0") // Get only the regular season games

val pointsCalc = udf((ownGoals: Int, opponentGoals: Int, lastGoalTime: Int) => {
  val points =
    if (ownGoals > opponentGoals && lastGoalTime <= 3600) 3 // Team scored more goals than the opponent during the regular 60 minutes
    else if (ownGoals > opponentGoals && lastGoalTime > 3600) 2 // The score line was even after 60 minutes but the team scored a winning goal during the extra time
    else if (ownGoals < opponentGoals && lastGoalTime > 3600) 1 // The score line was even after 60 minutes but the opponent scored a winning goal during the extra time
    else if (ownGoals == opponentGoals && lastGoalTime < 3600) 1 // There were no goals in the extra time
    else 0 // The opponent scored more goals than the team during the regular 60 minutes
  points
})

// Home games by season and team
val homeGameDF = regularGamesDF
  .withColumn("points", pointsCalc(col("homeTeamGoals"), col("awayTeamGoals"), col("lastGoalTime")))
  .groupBy("season", "homeTeamCode")
  .agg(
    count("*").alias("games"),
    sum(when(col("points") >= 2, 1).otherwise(0)).alias("wins"),
    sum(when(col("points") < 2, 1).otherwise(0)).alias("losses"),
    sum(col("homeTeamGoals")).alias("goalsScored"),
    sum(col("awayTeamGoals")).alias("goalsConceded"),
    sum(col("points")).alias("points")
  )
// Away games by season and team
val awayGameDF = regularGamesDF
      .withColumn("points", pointsCalc(col("awayTeamGoals"), col("homeTeamGoals"), col("lastGoalTime")))
      .groupBy("season", "awayTeamCode")
      .agg(
        count("*").alias("games"),
        sum(when(col("points") >= 2, 1).otherwise(0)).alias("wins"),
        sum(when(col("points") < 2, 1).otherwise(0)).alias("losses"),
        sum(col("awayTeamGoals")).alias("goalsScored"),
        sum(col("homeTeamGoals")).alias("goalsConceded"),
        sum(col("points")).alias("points")
      )

// Combine and aggregate the games to a single dataFrame
val regularSeasonDF: DataFrame = homeGameDF
  .withColumnRenamed("homeTeamCode", "teamCode")
  .union(
    awayGameDF
      .withColumnRenamed("awayTeamCode", "teamCode")
    )
  .groupBy("season", "teamCode")
  .agg(
    sum("games").alias("games"),
    sum("wins").alias("wins"),
    sum("losses").alias("losses"),
    sum("goalsScored").alias("goalsScored"),
    sum("goalsConceded").alias("goalsConceded"),
    sum("points").alias("points")
  )

println(s"Number of games in the DataFrame: '${regularSeasonDF.count()}'")
regularSeasonDF.show(10)


// COMMAND ----------

// MAGIC %md
// MAGIC ## Basic Task 7 - The worst regular season teams
// MAGIC
// MAGIC Using the regular season data frame created in the basic task 6, create a data frame containing the regular season records for the worst regular season team, i.e. the team with the least amount of points, for each season. You can assume that there are no ties for the lowest amount of points in each season.
// MAGIC
// MAGIC Finally, fetch the details for the worst regular season team in season 2022.
// MAGIC

// COMMAND ----------

// Find the worst team for each season
val worstTeamDF: DataFrame = regularSeasonDF.groupBy("season")
  .agg(
    min("points").alias("points")
  )

// Join with the regularSeasonDF to get the details of the worst team
val worstRegularTeams: DataFrame = worstTeamDF.join(regularSeasonDF,
  Seq("season", "points"),
  "inner"
)

worstRegularTeams.show()


// COMMAND ----------

val worstRegularTeam2022: Row = worstRegularTeams.filter("season = 2022").first()

println("Worst regular season team in 2022:")
println(s"    Team: ${worstRegularTeam2022.getAs[String]("teamCode")}")
println(s"    Games: ${worstRegularTeam2022.getAs[Long]("games")}")
println(s"    Wins: ${worstRegularTeam2022.getAs[Long]("wins")}")
println(s"    Losses: ${worstRegularTeam2022.getAs[Long]("losses")}")
println(s"    Goals scored: ${worstRegularTeam2022.getAs[Long]("goalsScored")}")
println(s"    Goals conceded: ${worstRegularTeam2022.getAs[Long]("goalsConceded")}")
println(s"    Points: ${worstRegularTeam2022.getAs[Long]("points")}")


// COMMAND ----------

// MAGIC %md
// MAGIC ## Additional tasks
// MAGIC
// MAGIC The implementation of the basic tasks is compulsory for every group.
// MAGIC
// MAGIC Doing the following additional tasks you can gain course points which can help in getting a better grade from the course (or passing the course).
// MAGIC Partial solutions can give partial points.
// MAGIC
// MAGIC The additional task 1 will be considered in the grading for every group based on their solutions for the basic tasks.
// MAGIC
// MAGIC The additional tasks 2 and 3 are separate tasks that do not relate to any other task in the assignment. The solutions used in these other additional tasks do not affect the grading of additional task 1. Instead, a good use of optimized methods can positively affect the grading of each specific task, while very non-optimized solutions can have a negative effect on the task grade.
// MAGIC

// COMMAND ----------

// MAGIC %md
// MAGIC ## Additional Task 1 - Optimized solutions to the basic tasks (2 points)
// MAGIC
// MAGIC Use the tools Spark offers effectively and avoid unnecessary operations in the code for the basic tasks.
// MAGIC
// MAGIC A couple of things to consider (**NOT** even close to a complete list):
// MAGIC
// MAGIC - Consider using explicit schemas when dealing with CSV data sources.
// MAGIC - Consider only including those columns from a data source that are actually needed.
// MAGIC - Filter unnecessary rows whenever possible to get smaller datasets.
// MAGIC - Avoid collect or similar expensive operations for large datasets.
// MAGIC - Consider using explicit caching if some data frame is used repeatedly.
// MAGIC - Avoid unnecessary shuffling (for example sorting) operations.
// MAGIC
// MAGIC It is okay to have your own test code that would fall into category of "ineffective usage" or "unnecessary operations" while doing the assignment tasks. However, for the final Moodle submission you should comment out or delete such code (and test that you have not broken anything when doing the final modifications).
// MAGIC
// MAGIC Note, that you should not do the basic tasks again for this additional task, but instead modify your basic task code with more efficient versions.
// MAGIC
// MAGIC You can create a text cell below this one and describe what optimizations you have done. This might help the grader to better recognize how skilled your work with the basic tasks has been.
// MAGIC

// COMMAND ----------

// MAGIC %md
// MAGIC Steps taken to optimize the solutions
// MAGIC - Schema is created for reading the csv file in Basic Task 1
// MAGIC - Unnecessary columns are removed  by dropping from DataFrames to reduce the amount of data that needs to be handled
// MAGIC - Unnecessary rows are removed by filtering from DataFrames to reduce the amount of data that needs to be handled
// MAGIC - DataFrames are created once and then read after that
// MAGIC - Tried to avoid using expensive operation like collect
// MAGIC - Unnecessary sortings are not done
// MAGIC
// MAGIC Otherwise the Basic Tasks are done as well and optimally as I know how to

// COMMAND ----------

// MAGIC %md
// MAGIC ## Additional Task 2 - Unstructured data (2 points)
// MAGIC
// MAGIC You are given some text files with contents from a few thousand random articles both in English and Finnish from Wikipedia. Content from English articles are in the [Shared container](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2Fe0c78478-e7f8-429c-a25f-015eae9f54bb%2FresourceGroups%2Ftuni-cs320-f2023-rg%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftunics320f2023gen2/path/shared/etag/%220x8DBB0695B02FFFE%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None) at folder `assignment/wikipedia/en` and content from Finnish articles are at folder `assignment/wikipedia/fi`.
// MAGIC
// MAGIC Some cleaning operations have already been done to the texts but the some further cleaning is still required.
// MAGIC
// MAGIC The final goal of the task is to get the answers to following questions:
// MAGIC
// MAGIC - What are the ten most common English words that appear in the English articles?
// MAGIC - What are the five most common 5-letter Finnish words that appear in the Finnish articles?
// MAGIC - What is the longest word that appears at least 150 times in the articles?
// MAGIC - What is the average English word length for the words appearing in the English articles?
// MAGIC - What is the average Finnish word length for the words appearing in the Finnish articles?
// MAGIC
// MAGIC For a word to be included in the calculations, it should fulfill the following requirements:
// MAGIC
// MAGIC - Capitalization is to be ignored. I.e., words "English", "ENGLISH", and "english" are all to be considered as the same word "english".
// MAGIC - An English word should only contain the 26 letters from the alphabet of Modern English. Only exception is that punctuation marks, i.e. hyphens `-`, are allowed in the middle of the words as long as there are no two consecutive punctuation marks without any letters between them.
// MAGIC - The only allowed 1-letter English words are `a` and `i`.
// MAGIC - A Finnish word should follow the same rules as English words, except that three additional letters, `å`, `ä`, and `ö`, are also allowed, and that no 1-letter words are allowed. Also, any word that contains "`wiki`" should not be considered as Finnish word.
// MAGIC
// MAGIC Some hints:
// MAGIC
// MAGIC - Using an RDD or a Dataset (in Scala) might make the data cleaning and word determination easier than using DataFrames.
// MAGIC - It can be assumed that in the source data each word in the same line is separated by at least one white space (` `).
// MAGIC - You are allowed to remove all non-allowed characters from the source data at the beginning of the cleaning process.
// MAGIC - It is advisable to first create a DataFrame/Dataset/RDD that contains the found words, their language, and the number of times those words appeared in the articles. This can then be used as the starting point when determining the answers to the given questions.
// MAGIC

// COMMAND ----------

// some constants that could be useful
val englishLetters: String = "abcdefghijklmnopqrstuvwxyz"
val finnishLetters: String = englishLetters + "åäö"
val whiteSpace: String = " "
val punctuationMark: Char = '-'
val twoPunctuationMarks: String = "--"
val allowedEnglishOneLetterWords: List[String] = List("a", "i")
val wikiStr: String = "wiki"

val englishStr: String = "English"
val finnishStr: String = "Finnish"


// COMMAND ----------

// Loading the wikipedia articles
val enArticles: RDD[String] = sc.textFile("abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/wikipedia/en")
val fiArticles: RDD[String] = sc.textFile("abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/wikipedia/fi")
/*
println(s"Number of lines in English: '${enArticles.count()}'")
println(s"Number of lines in Finnish: '${fiArticles.count()}'")
*/

// Function to clean and filter words
def cleanAndFilterWords(text: String, allowedLetters: String, oneLetterWords: List[String], lang: String): Seq[String] = {
  text.split("\\s+")
    .map(_.toLowerCase().replaceAll("[^" + allowedLetters + punctuationMark + "]", ""))
    .filter(word =>
      (word.length > 1) ||
      (word.length == 1 && oneLetterWords.contains(word) && !lang.equals(finnishStr)) ||
      //!(word.toLowerCase().contains(wikiStr) && lang.equals(finnishStr)) || // Does not work for some reason so we will filter the words out later from the dataframe
      (!word.contains(twoPunctuationMarks) && !word.equals("-")) // Filter out double punctuation marks and "words" that are only a hyphen
    )
    .filter(_.nonEmpty)  // Filter out empty strings
}

// Process English articles
val englishWords = enArticles
  .flatMap(line => cleanAndFilterWords(line, englishLetters, allowedEnglishOneLetterWords, englishStr))
  .map(word => (word, 1))
  .reduceByKey(_ + _)

// Process Finnish articles
val finnishWords = fiArticles
  .flatMap(line => cleanAndFilterWords(line, finnishLetters, List(), finnishStr))
  .map(word => (word, 1))
  .reduceByKey(_ + _)
/*
println(s"Number of words in English: '${englishWords.count()}'")
println(s"Number of words in Finnish: '${finnishWords.count()}'")
*/

// COMMAND ----------

val enwWordsDF: DataFrame = englishWords.toDF("word", "count")

val commonWordsEn: DataFrame = enwWordsDF.orderBy(col("count").desc).limit(10)

println("The ten most common English words that appear in the English articles:")
commonWordsEn.show()


// COMMAND ----------

val fiwWordsDF: DataFrame = finnishWords.toDF("word", "count").filter(!col("word").contains(wikiStr)) // Any word that contains "wiki" is filtered out of the finnish words

val common5LetterWordsFi: DataFrame = fiwWordsDF.filter(length(col("word")) === 5).orderBy(col("count").desc).limit(5)

println("The five most common 5-letter Finnish words that appear in the Finnish articles:")
common5LetterWordsFi.show()


// COMMAND ----------

val combinedDF: DataFrame = enwWordsDF.union(fiwWordsDF)

val longestWord: String = combinedDF
  .filter(col("count") >= 150)
  .orderBy(length(col("word")).desc)
  .limit(1)
  .first()
  .getAs[String]("word")

println(s"The longest word appearing at least 150 times is '${longestWord}'")

// Calculate the average lengths for the english and finnish words
val avgLengthEnglish: DataFrame = enwWordsDF
.agg(sum(length(col("word")) * col("count")).alias("totalLength"), sum(col("count")).alias("totalCount"))
.selectExpr("'English' as language", "round(totalLength / totalCount, 2) as average_word_length")

val avgLengthFinnish: DataFrame = fiwWordsDF
.agg(sum(length(col("word")) * col("count")).alias("totalLength"), sum(col("count")).alias("totalCount"))
.selectExpr("'Finnish' as language", "round(totalLength / totalCount, 2) as average_word_length")

// Create a union of the results for presentation
val averageWordLengths: DataFrame = avgLengthFinnish.union(avgLengthEnglish)

println("The average word lengths:")
averageWordLengths.show()


// COMMAND ----------

// MAGIC %md
// MAGIC ## Additional Task 3 - K-Means clustering (2 points)
// MAGIC
// MAGIC You are given a dataset containing the locations of building in Finland. The dataset is a subset from [https://www.avoindata.fi/data/en_GB/dataset/postcodes/resource/3c277957-9b25-403d-b160-b61fdb47002f](https://www.avoindata.fi/data/en_GB/dataset/postcodes/resource/3c277957-9b25-403d-b160-b61fdb47002f) limited to only postal codes with the first two numbers in the interval 30-44 ([postal codes in Finland](https://www.posti.fi/en/zip-code-search/postal-codes-in-finland)). The dataset is in the [Shared container](https://portal.azure.com/#view/Microsoft_Azure_Storage/ContainerMenuBlade/~/overview/storageAccountId/%2Fsubscriptions%2Fe0c78478-e7f8-429c-a25f-015eae9f54bb%2FresourceGroups%2Ftuni-cs320-f2023-rg%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Ftunics320f2023gen2/path/shared/etag/%220x8DBB0695B02FFFE%22/defaultEncryptionScope/%24account-encryption-key/denyEncryptionScopeOverride~/false/defaultId//publicAccessVal/None) at folder `assignment/buildings.parquet`.
// MAGIC
// MAGIC [K-Means clustering](https://en.wikipedia.org/wiki/K-means_clustering) algorithm is an unsupervised machine learning algorithm that can be used to partition the input data into k clusters. Your task is to use the Spark ML library and its K-Means clusterization algorithm to divide the buildings into clusters using the building coordinates `latitude_wgs84` and `longitude_wgs84` as the basis of the clusterization. You should implement the following procedure:
// MAGIC
// MAGIC 1. Start with all the buildings in the dataset.
// MAGIC 2. Divide the buildings into seven clusters with K-Means algorithm using `k=7` and the longitude and latitude of the buildings.
// MAGIC 3. Find the cluster to which the Sähkötalo building from the Hervanta campus is sorted into. The building id for Sähkötalo in the dataset is `102363858X`.
// MAGIC 4. Choose all the buildings from the cluster with the Sähkötalo building.
// MAGIC 5. Find the cluster center for the chosen cluster of buildings.
// MAGIC 6. Calculate the largest distance from a building in the chosen cluster to the chosen cluster center. You are given a function `haversine` that you can use to calculate the distance between two points using the latitude and longitude of the points.
// MAGIC 7. While the largest distance from a building in the considered cluster to the cluster center is larger than 3 kilometers run the K-Means algorithm again using the following substeps.
// MAGIC     - Run the K-Means algorithm to divide the remaining buildings into smaller clusters. The number of the new clusters should be one less than in the previous run of the algorithm (but should always be at least two). I.e., the sequence of `k` values starting from the second run should be 6, 5, 4, 3, 2, 2, ...
// MAGIC     - After using the algorithm again, choose the new smaller cluster of buildings so that it includes the Sähkötalo building.
// MAGIC     - Find the center of this cluster and calculate the largest distance from a building in this cluster to its center.
// MAGIC
// MAGIC As the result of this process, you should get a cluster of buildings that includes the Sähkötalo building and in which all buildings are within 3 kilometers of the cluster center.
// MAGIC
// MAGIC Using the final cluster, find the answers to the following questions:
// MAGIC
// MAGIC - How many buildings in total are in the final cluster?
// MAGIC - How many Hervanta buildings are in this final cluster? (A building is considered to be in Hervanta if their postal code is `33720`)
// MAGIC
// MAGIC Some hints:
// MAGIC
// MAGIC - Once you have trained a KMeansModel, the coordinates for the cluster centers, and the cluster indexes for individual buildings can be accessed through the model object (`clusterCenters`, `summary.predictions`).
// MAGIC - The given haversine function for calculating distances can be used with data frames if you turn it into an user defined function.
// MAGIC

// COMMAND ----------

// some helpful constants
val startK: Int = 7
val seedValue: Long = 1

// the building id for Sähkötalo building at Hervanta campus
val hervantaBuildingId: String = "102363858X"
val hervantaPostalCode: Int = 33720

val maxAllowedClusterDistance: Double = 3.0


// returns the distance between points (lat1, lon1) and (lat2, lon2) in kilometers
// based on https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
def haversine(lat1: Double, lon1: Double, lat2: Double, lon2: Double): Double = {
    val R: Double = 6378.1  // radius of Earth in kilometers
    val phi1 = scala.math.toRadians(lat1)
    val phi2 = scala.math.toRadians(lat2)
    val deltaPhi = scala.math.toRadians(lat2 - lat1)
    val deltaLambda = scala.math.toRadians(lon2 - lon1)

    val a = scala.math.sin(deltaPhi * deltaPhi / 4.0) +
        scala.math.cos(phi1) * scala.math.cos(phi2) * scala.math.sin(deltaLambda * deltaLambda / 4.0)

    2 * R * scala.math.atan2(scala.math.sqrt(a), scala.math.sqrt(1 - a))
}


// COMMAND ----------


val buildingDF: DataFrame = spark.read.parquet("abfss://shared@tunics320f2023gen2.dfs.core.windows.net/assignment/buildings.parquet")

val featureCols = Array("latitude_wgs84", "longitude_wgs84")
val assembler = new VectorAssembler().setInputCols(featureCols).setOutputCol("features")
val assembledBuildings = assembler.transform(buildingDF)

// Init variables
var k = startK
var currentCluster = assembledBuildings

breakable {
  while (true) {
    // Run K-Means
    val kmeans = new KMeans().setK(k).setSeed(seedValue).setFeaturesCol("features").setPredictionCol(s"cluster_$k")
    val model = kmeans.fit(currentCluster)
    val clusterCenters = model.clusterCenters
    val predictions = model.transform(currentCluster)

    // Find the cluster of the Sähkötalo building
    val sahkolaloCluster = predictions.filter(col("building_id") === hervantaBuildingId).select(s"cluster_$k").first().getInt(0)
    currentCluster = predictions.filter(col(s"cluster_$k") === sahkolaloCluster)

    // Find cluster center and calculate largest distance
    val clusterCenter = clusterCenters(sahkolaloCluster)
    val calculateDistance = udf((lat: Double, lon: Double) => haversine(lat, lon, clusterCenter(0), clusterCenter(1)))
    val distances = currentCluster.withColumn("distance", calculateDistance(col("latitude_wgs84"), col("longitude_wgs84")))
    val maxDistance = distances.agg(max("distance")).first().getDouble(0)

    // Check if the largest distance is smaller than 3 kilometers
    if (maxDistance <= maxAllowedClusterDistance) {
      // Final cluster found
      break
    }

    // Reduce k for the next iteration
    k = math.max(k - 1, 2)
  }
}


val finalCluster: DataFrame = currentCluster

val clusterBuildingCount: Long = finalCluster.count()
val clusterHervantaBuildingCount: Long = currentCluster.filter(col("postal_code") === hervantaPostalCode).count()

println(s"Buildings in the final cluster: ${clusterBuildingCount}")
print(s"Hervanta buildings in the final cluster: ${clusterHervantaBuildingCount} ")
println(s"(${scala.math.round(10000.0*clusterHervantaBuildingCount/clusterBuildingCount)/100.0}% of all buildings in the final cluster)")
println("===========================================================================================")


// COMMAND ----------



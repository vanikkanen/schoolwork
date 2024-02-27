// Datastructures.cc
//
// Student name: Valtteri Nikkanen
// Student email: valtteri.nikkanen@tuni.fi
// Student number: 282688

#include "datastructures.hh"

#include <iostream>
#include <list>
#include <random>

#include <cmath>
#include <ostream>
#include <stdexcept>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>

std::minstd_rand rand_engine; // Reasonably quick pseudo-random generator

template <typename Type>
Type random_in_range(Type start, Type end)
{
    auto range = end-start;
    ++range;

    auto num = std::uniform_int_distribution<unsigned long int>(0, range-1)(rand_engine);

    return static_cast<Type>(start+num);
}

// Modify the code below to implement the functionality of the class.
// Also remove comments from the parameter names when you implement
// an operation (Commenting out parameter name prevents compiler from
// warning about unused parameters on operations you haven't yet implemented.)
/*!
 * \brief Datastructures::Datastructures initializes the datastructure
 */
Datastructures::Datastructures()
{
    // Write any initialization you need here
}
/*!
 * \brief Datastructures::~Datastructuresdoes the required cleanup when the
 *        datastrucutre is destroyed
 */
Datastructures::~Datastructures()
{
    // Write any cleanup you need here
}
/*!
 * \brief Datastructures::station_count counts the number of stations in the
 * data structure
 * \return the number of stations
 */
unsigned int Datastructures::station_count()
{
    // Return the number of stations in the datastructure
    return all_stations_map.size();
}
/*!
 * \brief Datastructures::clear_all clears the data structure of all stations
 * and regions
 */
void Datastructures::clear_all()
{
    all_stations_map.clear();
    all_regions_map.clear();
}
/*!
 * \brief Datastructures::all_stations returns all the stations in the data
 * structure
 * \return a vector containing the StationID of all the stations in the
 * datastructure
 */
std::vector<StationID> Datastructures::all_stations()
{
    std::vector<StationID> all_stations;
    all_stations.reserve(all_stations_map.size());
    for(auto const& station : all_stations_map) {
        all_stations.push_back(station.first);
    }
    return all_stations;
}
/*!
 * \brief Datastructures::add_station adds a new station to the data strucutre
 * \param id of the new station to be added
 * \param name of the new station to be added
 * \param xy coord of the new station to be added
 * \return true if insertion was succesfull, false if it wasnt
 */
bool Datastructures::add_station(StationID id, const Name& name, Coord xy)
{
    struct Station new_station = {id, name, xy};
    bool ok = all_stations_map.insert({id, new_station}).second;
    /*
    sort_station_name_map.insert({id, name});
    sort_station_coord_map.insert({id, xy});
    */
    return ok;
}
/*!
 * \brief Datastructures::get_station_name returns the name of the station
 * \param id is the StationID of the station whose name is wanted
 * \return name of the station or NO_NAME if the station wasnt found in the
 *         datastructure
 */
Name Datastructures::get_station_name(StationID id)
{
    try {
        return all_stations_map.at(id).name;
    }
    catch (const std::out_of_range& e) {
        return NO_NAME;
    }
}
/*!
 * \brief Datastructures::get_station_coordinates returns the coordinates of the
 *        station
 * \param id is the StationID of the station whose coordinate is wanted
 * \return coordinate of the station or NO_COORD if the station wasnt found in
 *         the datastructure
 */
Coord Datastructures::get_station_coordinates(StationID id)
{
    try {
        return all_stations_map.at(id).coord;
    }
    catch (const std::out_of_range& e) {
        return NO_COORD;
    }
}

/*!
 * \brief Datastructures::stations_alphabetically returns all the stations in
 *        the datastructures in alphabetical order
 * \return a vector containing all the StationIDs in their names alphabetical
 *         order
 */
std::vector<StationID> Datastructures::stations_alphabetically()
{
    std::vector<StationID> stations = all_stations();
    auto comp = [this](StationID a, StationID b) {
        return all_stations_map[a].name < all_stations_map[b].name;
    };
    std::sort(stations.begin(), stations.end(), comp);

    return stations;
}
/*!
 * \brief Datastructures::stations_distance_increasing returns all the stations
 *          in the datastructures in increasing order by their distance from
 *          the coordinate (0,0)
 * \return a vector containing all the StationIDs in increasing order by their
 *         distance from the coordinate (0,0)
 */
std::vector<StationID> Datastructures::stations_distance_increasing()
{
    {
        std::vector<StationID> stations = all_stations();
        auto comp = [this](StationID a, StationID b)-> bool {
            /*
            double dist_a = hypot(sort_station_coord_map.at(a).x,
                                  sort_station_coord_map.at(a).y);
            double dist_b = hypot(sort_station_coord_map.at(b).x,
                                  sort_station_coord_map.at(b).y);
                                  */
            double dist_a = hypot(all_stations_map.at(a).coord.x,
                                  all_stations_map.at(a).coord.y);
            double dist_b = hypot(all_stations_map.at(b).coord.x,
                                  all_stations_map.at(b).coord.y);
        return dist_a < dist_b;
        };


        std::sort(stations.begin(), stations.end(), comp);

        return stations;
    }
}
/*!
 * \brief Datastructures::find_station_with_coord finds a station with the given
 *        coordinate
 * \param xy is coordinate that the station in is wanted
 * \return StationID of the found station in the given coordinate or NO_STATION
 *         if no station was found
 */
StationID Datastructures::find_station_with_coord(Coord xy)
{
    for (auto& it : all_stations_map) {
        if(it.second.coord == xy) {
            return it.first;
        }
    }
    return NO_STATION;
}
/*!
 * \brief Datastructures::change_station_coord changes the coord of the given
 *        station
 * \param id is the StationID of the station whose coord is to be changed
 * \param newcoord is the neew coordinate of the station
 * \return true if the station was found and coordinate changed or false if
 *         the station was not found in the datastructure
 */
bool Datastructures::change_station_coord(StationID id, Coord newcoord)
{
    // Check if station in map
    if (all_stations_map.find(id) != all_stations_map.end()) {
        all_stations_map.at(id).coord = newcoord;
        //sort_station_coord_map.at(id) = newcoord;
        return true;
    }
    return false;
}
/*!
 * \brief Datastructures::add_departure adds a departure to the station for a
 *        given train for a given time
 * \param station_id is the StationID of the station where the departure is to
 *        be added
 * \param train_id is the TrainID of the train whose departure is to be added
 * \param time is the time of the departure for the train on the station
 * \return true if the departure was added succesfully, or false if no station
 *         was found or if the same departure was found already for the station
 */
bool Datastructures::add_departure(
                            StationID station_id, TrainID train_id, Time time)
{
    if (all_stations_map.find(station_id) != all_stations_map.end()) {
        std::pair<Time, TrainID> new_departure = {time, train_id};
        std::vector<std::pair<Time, TrainID>> departures =
                all_stations_map.at(station_id).departures;
        if (std::find(departures.begin(), departures.end(),
                      new_departure) == departures.end()) {
            all_stations_map.at(station_id).departures.push_back(new_departure);
            return true;
        }
    }
    return false;
}
/*!
 * \brief Datastructures::remove_departure removes a departure from the station
 * \param station_id is the StationID from where the departure is to be removed
 * \param train_id is the TrainID whose departure is to be removed
 * \param time is the Time of the departure of which is to be removed
 * \return returns true if the removal was succesfull or false if the station
 *         wasnt found or if the departure to be removed wasnt found in that
 *         station
 */
bool Datastructures::remove_departure(
                            StationID station_id, TrainID train_id, Time time)
{
    if (all_stations_map.find(station_id) != all_stations_map.end()) {
        std::pair<Time, TrainID> new_departure = {time, train_id};
        std::vector<std::pair<Time, TrainID>> departures =
                all_stations_map.at(station_id).departures;
        auto to_erase = std::find(departures.begin(),
                                  departures.end(), new_departure);
        if (to_erase != departures.end()) {
            all_stations_map.at(station_id).departures.erase(to_erase);
            return true;
        }
    }
    return false;
}
/*!
 * \brief Datastructures::station_departures_after returns all the departures
 *        for a given station that depart after the given time
 * \param station_id is the StationID of the station whose departures are wanted
 * \param time is the Time after whioch the departures are wanted
 * \return a vector containing all the Time and TrainID pairs of the departures
 *         at the station after the given time or a vector containing NO_TIME,
 *         NO_TRAIN pair if no station was found for the given StationID or an
 *         empty vector if no departures were found after the given time
 */
std::vector<std::pair<Time, TrainID>> Datastructures::station_departures_after(
                                                StationID station_id, Time time)
{
    if (all_stations_map.find(station_id) != all_stations_map.end()) {
        std::vector<std::pair<Time, TrainID>> departures
                = all_stations_map.at(station_id).departures;
        if (departures.empty()) {
            return std::vector<std::pair<Time, TrainID>>();
        }
        std::sort(departures.begin(), departures.end(),
                  [](std::pair<Time, TrainID> a,
                     std::pair<Time, TrainID> b) -> bool {
            return (a.first < b.first) ||
                   ((a.first == b.first) && (a.second < b.second));
        });
        auto it = std::find_if(departures.begin(), departures.end(),
                  [time](std::pair<Time, TrainID> a){return a.first >= time;});
        if (it != departures.end()) {
            std::vector<std::pair<Time, TrainID>> to_return(it, departures.end());
            return to_return;
        }
        else {
            return std::vector<std::pair<Time, TrainID>>();
        }
    }
    std::pair<Time, TrainID> no_station {NO_TIME, NO_STATION};
    std::vector<std::pair<Time, TrainID>> to_return {no_station};
    return to_return;
}
/*!
 * \brief Datastructures::add_region adds a region to the datastructure
 * \param id is the RegionID of the new region
 * \param name is the Name of the new station
 * \param coords is the vector containing the coordinates of the new region
 * \return true if the insertion was succesfull or false if it wasnt
 */
bool Datastructures::add_region(
                    RegionID id, const Name &name, std::vector<Coord> coords)
{
    struct Region new_region = {id, name, coords};
    bool ok = all_regions_map.insert({id, new_region}).second;
    return ok;
}
/*!
 * \brief Datastructures::all_regions returns all the regions in the
 *        datastructure
 * \return a vector containing all the regions RegionIds that are in the
 *         datastructure
 */
std::vector<RegionID> Datastructures::all_regions()
{
    std::vector<RegionID> all_regions;
    all_regions.reserve(all_regions_map.size());
    for(auto const& region : all_regions_map) {
        all_regions.push_back(region.first);
    }
    return all_regions;
}
/*!
 * \brief Datastructures::get_region_name return the name of the region
 * \param id is the RegionId whose name is wanted
 * \return the Name of the region or NO_NAME if no region was found for the
 *         given RegionID
 */
Name Datastructures::get_region_name(RegionID id)
{
    try {
        return all_regions_map.at(id).name;
    }
    catch (const std::out_of_range& e) {
        return NO_NAME;
    }
}
/*!
 * \brief Datastructures::get_region_coords return the coordinates of the region
 * \param id is the RegionId whose coordinates are wanted
 * \return a vector containing the coordinates of the region or NO_COORD if no
 *         region was found for the given RegionID
 */
std::vector<Coord> Datastructures::get_region_coords(RegionID id)
{
    try {
        return all_regions_map.at(id).coords;
    }
    catch (const std::out_of_range& e) {
        return std::vector<Coord>{NO_COORD};
    }
}
/*!
 * \brief Datastructures::add_subregion_to_region adds a subregion to the region
 * \param id is the RegionID of the region that is to be added as a subregion
 * \param parent_id is the RegionID of the region where the other region is to
 *        be added as a subregion
 * \return returns true if the add was succesfull or false if no region was
 *         found for either of the RegionIDs or if the region to be added as a
 *         subregion already had a parent region
 */
bool Datastructures::add_subregion_to_region(RegionID id, RegionID parent_id)
{
    try {
        Region & region = all_regions_map.at(id);
        Region & parent_region = all_regions_map.at(parent_id);
        if (region.parent_region == NO_REGION) {
            region.parent_region = parent_id;
            parent_region.subregions.push_back(id);
            return true;
        }
        return false;
    }
    catch (const std::out_of_range& e){
        return false;
    }
}
/*!
 * \brief Datastructures::add_station_to_region adds a station to a region
 * \param station_id is the StationID of the region that is to be added to the
 *        region
 * \param region_id is the RegionID where the station is to be added
 * \return true if the add was succesfull or false if no station or region was
 *         found for their given ids or if the station was already assigned to
 *         a region
 */
bool Datastructures::add_station_to_region(
                                    StationID station_id, RegionID region_id)
{
    try {
        Station & station = all_stations_map.at(station_id);
        Region & region = all_regions_map.at(region_id);
        if (station.region == NO_REGION) {
            station.region = region.region_id;
            region.stations.push_back(station.station_id);
            return true;
        }
        return false;
    }
    catch (const std::out_of_range& e){
        return false;
    }
}
/*!
 * \brief Datastructures::station_in_regions returns all the regions where the
 *        station belongs wither directly or indirectly
 * \param id is the StationID of the station whose regions are wanted
 * \return a vector cointaining all the RegionIDs where the station belongs.
 *         Returns an empty vector if the station has no region. Returns a
 *         vector containing NO_REGION if no station was found for the given id
 */
std::vector<RegionID> Datastructures::station_in_regions(StationID id)
{
    try {
        RegionID region_id = all_stations_map.at(id).region;
        if (region_id == NO_REGION) {
            return std::vector<RegionID>();
        }
        std::vector<RegionID> regions = get_parent_regions(region_id);
        return regions;
    }
    catch (const std::out_of_range& e){
        return std::vector<RegionID>{NO_REGION};
    }
}
/*!
 * \brief Datastructures::all_subregions_of_region returns all the direct or
 *        indirect subregions of a region
 * \param id is the RegionID of the region whose subregions are wanted
 * \return a vector containing all the RegionIDs of the subregions of the given
 *         region or a vector containing NO_REGION if no region with the id was
 *         found
 */
std::vector<RegionID> Datastructures::all_subregions_of_region(RegionID id)
{
    try {
        Region region = all_regions_map.at(id);
        std::vector<RegionID> subregions;
        get_subregions(region, subregions);
        return subregions;
    }
    catch (const std::out_of_range& e){
        return std::vector<RegionID>{NO_REGION};
    }
}
/*!
 * \brief Datastructures::stations_closest_to returns the 3 closest stations to
 *        the given coordinate or less stations if there are less than 3
 *        stations in the datastructure
 * \param xy is the coordinate to where the 3 closest stations are wanted
 * \return a vector containing the 3 or less stations closest to the coordinate
 */
std::vector<StationID> Datastructures::stations_closest_to(Coord xy)
{
    std::vector<StationID> stations = all_stations();

    auto comp = [xy, this](StationID a, StationID b) {
        float dist_a = std::sqrt(
                        std::pow(xy.x-all_stations_map.at(a).coord.x, 2) +
                        std::pow(xy.y-all_stations_map.at(a).coord.y, 2));
        float dist_b = std::sqrt(
                        std::pow(xy.x-all_stations_map.at(b).coord.x, 2) +
                        std::pow(xy.y-all_stations_map.at(b).coord.y, 2));
        return dist_a > dist_b;
    };

    int station_nro = 3;
    if (stations.size() < 3) {
        station_nro = stations.size();
    }
    std::make_heap(stations.begin(), stations.end(), comp);
    std::vector<StationID> to_return;
    for (int i = 0; i < station_nro; ++i) {
        std::pop_heap(stations.begin(), stations.end(), comp);
        to_return.push_back(stations.back());
        stations.pop_back();
    }
    return to_return;
}
/*!
 * \brief Datastructures::remove_station removes a station from the
 *        datastructure
 * \param station_id is the StationID of the station that is to be removed
 * \return true if the removal was succesfull or false if no station for the id
 *         was found
 */
bool Datastructures::remove_station(StationID station_id)
{
    try {       
        RegionID region_id = all_stations_map.at(station_id).region;
        if (region_id != NO_REGION) {
            Region & region = all_regions_map.at(region_id);
            std::vector<StationID> stations = region.stations;
            stations.erase(std::find(stations.begin(), stations.end(), station_id));
            region.stations = stations;
        }
        all_stations_map.erase(station_id);
        return true;
    }
    catch (const std::out_of_range& e){
        return false;
    }
}
/*!
 * \brief Datastructures::common_parent_of_regions returns the closest parent
 * region of the given regions
 * \param id1 is the RegionID of the first region
 * \param id2 is the RegionID of the second region
 * \return returns the RegionID of the closest parent or NO_REGION if no region
 *         was found for either of the region ids or if no common parent for
 *         the regions was found
 */
RegionID Datastructures::common_parent_of_regions(RegionID id1, RegionID id2)
{
    try {
        Region region1 = all_regions_map.at(id1);
        Region region2 = all_regions_map.at(id2);
        std::vector<RegionID> parent_regions1 = get_parent_regions(region1.region_id);

        std::unordered_set<RegionID>parent_set1(parent_regions1.begin()+1,
                                                parent_regions1.end());

        while(region2.parent_region != NO_REGION) {
            if (parent_set1.find(region2.parent_region) != parent_set1.end()) {
                return region2.parent_region;
            }
            region2 = all_regions_map.at(region2.parent_region);
        }
        return NO_REGION;
    }
    catch (const std::out_of_range& e){
        return NO_REGION;
    }
}

// Datastructures.hh
//
// Student name:
// Student email:
// Student number:

#ifndef DATASTRUCTURES_HH
#define DATASTRUCTURES_HH

#include <queue>
#include <string>
#include <vector>
#include <tuple>
#include <utility>
#include <limits>
#include <functional>
#include <exception>
#include <cmath>
#include <functional>

// Types for IDs
using StationID = std::string;
using TrainID = std::string;
using RegionID = unsigned long long int;
using Name = std::string;
using Time = unsigned short int;

// Return values for cases where required thing was not found
StationID const NO_STATION = "---";
TrainID const NO_TRAIN = "---";
RegionID const NO_REGION = -1;
Name const NO_NAME = "!NO_NAME!";
Time const NO_TIME = 9999;

// Return value for cases where integer values were not found
int const NO_VALUE = std::numeric_limits<int>::min();


// Type for a coordinate (x, y)
struct Coord
{
    int x = NO_VALUE;
    int y = NO_VALUE;
};

// Example: Defining == and hash function for Coord so that it can be used
// as key for std::unordered_map/set, if needed
inline bool operator==(Coord c1, Coord c2) { return c1.x == c2.x && c1.y == c2.y; }
inline bool operator!=(Coord c1, Coord c2) { return !(c1==c2); } // Not strictly necessary

struct CoordHash
{
    std::size_t operator()(Coord xy) const
    {
        auto hasher = std::hash<int>();
        auto xhash = hasher(xy.x);
        auto yhash = hasher(xy.y);
        // Combine hash values (magic!)
        return xhash ^ (yhash + 0x9e3779b9 + (xhash << 6) + (xhash >> 2));
    }
};

// Example: Defining < for Coord so that it can be used
// as key for std::map/set
inline bool operator<(Coord c1, Coord c2)
{
    if (c1.y < c2.y) { return true; }
    else if (c2.y < c1.y) { return false; }
    else { return c1.x < c2.x; }
}

// Return value for cases where coordinates were not found
Coord const NO_COORD = {NO_VALUE, NO_VALUE};

// Type for a distance (in metres)
using Distance = int;

// Return value for cases where Distance is unknown
Distance const NO_DISTANCE = NO_VALUE;

// This exception class is there just so that the user interface can notify
// about operations which are not (yet) implemented
class NotImplemented : public std::exception
{
public:
    NotImplemented() : msg_{} {}
    explicit NotImplemented(std::string const& msg) : msg_{msg + " not implemented"} {}

    virtual const char* what() const noexcept override
    {
        return msg_.c_str();
    }
private:
    std::string msg_;
};


// This is the class you are supposed to implement

class Datastructures
{
public:
    Datastructures();
    ~Datastructures();

    // Estimate of performance: O(1)
    // Short rationale for estimate: The complexity of reading athe size of a
    // map is constant
    unsigned int station_count();

    // Estimate of performance: O(n)
    // Short rationale for estimate: map.clear() has a linear complexity and
    // this does it twice
    void clear_all();

    // Estimate of performance: O(n)
    // Short rationale for estimate: This function loops through the map with
    // all the stations once pushes the StationIds to the vecotr and then
    // returns it. By allocating enough space from the start vector.push_back
    // is alaways constant time
    std::vector<StationID> all_stations();

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.insert() has these
    // complexitites in this use case
    bool add_station(StationID id, Name const& name, Coord xy);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear.
    Name get_station_name(StationID id);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear.
    Coord get_station_coordinates(StationID id);

    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: O(nlogn)
    // Short rationale for estimate: The sort algorithm is O(nlogn) in
    // complexity and it is the slowest thing
    std::vector<StationID> stations_alphabetically();

    // Estimate of performance: O(nlogn)
    // Short rationale for estimate: The sort algorithm is O(nlogn) in
    // complexity and it is the slowest thing
    std::vector<StationID> stations_distance_increasing();

    // Estimate of performance: O(n)
    // Short rationale for estimate: We need to loop through the map structure
    // to find the correct station. Best case its the first one and the function
    // is in constant time, worst case there is no station with the given coord
    // and its linear
    StationID find_station_with_coord(Coord xy);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: The most time consuming is the
    // unordered_map.find(), everything else is constant. unordered_map.at() is
    // also the same as find in its complexity
    bool change_station_coord(StationID id, Coord newcoord);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Every algortihm is linear at worst so the
    // whole function is in linear time at worst
    bool add_departure(StationID stationid, TrainID trainid, Time time);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Only linear functions are called. May be
    // faster if all hit best cases
    bool remove_departure(StationID stationid, TrainID trainid, Time time);

    // Estimate of performance: O(nlogn)
    // Short rationale for estimate: Sorting a vector is a nlogn complexity and
    // it is the slowest part of this function
    std::vector<std::pair<Time, TrainID>> station_departures_after(StationID stationid, Time time);

    // We recommend you implement the operations below only after implementing the ones above

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.insert() has these
    // complexitites and it is the slowest here
    bool add_region(RegionID id, Name const& name, std::vector<Coord> coords);

    // Estimate of performance: O(n)
    // Short rationale for estimate: This function loops through the map with
    // all the regions once pushes the RegionIds to the vecotr and then returns
    // it. By allocating enough space from the start vector.push_back is alaways
    // constant time
    std::vector<RegionID> all_regions();

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear.
    Name get_region_name(RegionID id);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear.
    std::vector<Coord> get_region_coords(RegionID id);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear.
    bool add_subregion_to_region(RegionID id, RegionID parentid);

    // Estimate of performance: Θ(1), O(n)
    // Short rationale for estimate: unordered_map.at() is on average constant
    // but its worst case is linear. Same goes for vector.push_back() which is
    // on average constant and linear if it needs to allocate more space
    bool add_station_to_region(StationID id, RegionID parentid);

    // Estimate of performance: O(n)
    // Short rationale for estimate: At most we are doing linear operations
    std::vector<RegionID> station_in_regions(StationID id);

    // Non-compulsory operations

    // Estimate of performance: O(n)
    // Short rationale for estimate: We walk through all the subregions of the
    // given region once to check if they have subregions themselves
    std::vector<RegionID> all_subregions_of_region(RegionID id);

    // Estimate of performance: O(nlog(n))
    // Short rationale for estimate: Some of the heap operations are logarithmic
    // in complexity and the compare function has a worst case of linear
    std::vector<StationID> stations_closest_to(Coord xy);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Only linear operations are performed.
    bool remove_station(StationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: Only linear operations are performed.
    RegionID common_parent_of_regions(RegionID id1, RegionID id2);

    //
    // New assignment 2 operations
    //

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: The worst case while we are looping through
    // all the stations and run into a worst case in unorder_map.at which is linear
    bool add_train(TrainID trainid, std::vector<std::pair<StationID, Time>> stationtimes);

    // Estimate of performance: O(n)
    // Short rationale for estimate: unordered_map.at is at worst linear
    std::vector<StationID> next_stations_from(StationID id);

    // Estimate of performance: O(n)
    // Short rationale for estimate: unordered_map.at is at worst linear
    std::vector<StationID> train_stations_from(StationID stationid, TrainID trainid);

    // Estimate of performance: O(n)
    // Short rationale for estimate: We loop through all the stations and tell
    // them that the vectors conatining iniformation about the trains are empty
    void clear_trains();

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: BFS is linear but unordered_map.at is also
    // linear in its worst case so we go to quadratic at the worst case. Average
    // should be linear
    std::vector<std::pair<StationID, Distance>> route_any(StationID fromid, StationID toid);

    // Non-compulsory operations

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: BFS is linear but unordered_map.at is also
    // linear in its worst case so we go to quadratic at the worst case. Average
    // should be linear
    std::vector<std::pair<StationID, Distance>> route_least_stations(StationID fromid, StationID toid);

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: DFS is linear but unordered_map.at is also
    // linear in its worst case so we go to quadratic at the worst case. Average
    // should be linear
    std::vector<StationID> route_with_cycle(StationID fromid);

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: Dijkstras algorith is nlogn. But something
    // might go wrong and some worst case worsens our efficiency.
    std::vector<std::pair<StationID, Distance>> route_shortest_distance(StationID fromid, StationID toid);

    // Estimate of performance: O(n^2)
    // Short rationale for estimate: Dijkstras algorith is nlogn. But something
    // might go wrong and some worst case worsens our efficiency
    std::vector<std::pair<StationID, Time>> route_earliest_arrival(StationID fromid, StationID toid, Time starttime);

private:

    // Struct for stations
    struct Station
    {
        StationID station_id;
        Name name;
        Coord coord;
        std::vector<std::pair<Time, TrainID>> departures = std::vector<std::pair<Time, TrainID>>();
        RegionID region = NO_REGION;
        std::vector<StationID> next_stations = std::vector<StationID>();
        std::unordered_map<StationID, std::unordered_map<StationID, std::pair<Time, TrainID>>> departure_times =
                std::unordered_map<StationID, std::unordered_map<StationID, std::pair<Time, TrainID>>>();
    };

    struct Region {
        RegionID region_id;
        Name name;
        std::vector<Coord> coords;
        RegionID parent_region = NO_REGION;
        std::vector<RegionID> subregions = std::vector<RegionID>();
        std::vector<StationID> stations = std::vector<StationID>();
    };

    // Struct for trains
    struct Train {
        TrainID train_id;
        std::vector<StationID> stations;
        std::unordered_map<Time, StationID> stations_by_time;
        StationID final_station;
    };

    // Unordered map for storing all the stations by their StationID
    std::unordered_map<StationID, Station> all_stations_map;
    /*
    // Help structures for functions
    std::unordered_map<StationID, Name> sort_station_name_map;
    std::unordered_map<StationID, Coord> sort_station_coord_map;
    */
    // Unordered map for storing all the regions by their RegionID
    std::unordered_map<RegionID, Region> all_regions_map;

    // Unordered map for storing all the trains
    std::unordered_map<TrainID, Train> all_trains_map;

    // Function for finding all the parent regions of a region
    /*!
     * \brief get_parent_regions returns parent regions of the given region
     * Complexity: O(n)
     * \param region_id of the region whose parent regions are wanted
     * \return a vector which contains the region and its parent regions
     */
    std::vector<RegionID> get_parent_regions(RegionID region_id) {
        std::vector<RegionID> regions;
        // Reserve enough space to avoid having to reallocate
        regions.reserve(all_regions_map.size());
        regions.push_back(region_id);
        while(all_regions_map.at(region_id).parent_region != NO_REGION) {
            Region region = all_regions_map.at(region_id);
            region_id = all_regions_map.at(region.parent_region).region_id;
            regions.push_back(region_id);
        }
        // Shrink the vector to correct size to save memory
        regions.shrink_to_fit();
        return regions;
    }
    /*!
     * \brief get_subregions recursive function to get all the subregions of a
     * region
     * \param region is the region whose subregions are to be added to the
     * vector
     * \param subregions is a vector containing the RegionIDs of all the
     * subregions and where this regions subregions are to be added
     */
    void get_subregions(Region region, std::vector<RegionID>& subregions) {
        for (auto subregion_id: region.subregions) {
            subregions.push_back(subregion_id);
            Region subregion = all_regions_map.at(subregion_id);
            get_subregions(subregion, subregions);
        }
    }

    // Struct for traversing through the stations
    struct StationNode {
        StationID station_id;
        Coord coord;
        std::vector<StationID> next_stations = std::vector<StationID>();
        std::unordered_map<StationID, std::unordered_map<StationID, std::pair<Time, TrainID>>> departure_times =
                std::unordered_map<StationID, std::unordered_map<StationID, std::pair<Time, TrainID>>>();
        StationID prev = NO_STATION;
        char color = 'w';
        int cost = -1;
    };

    /*!
     * \brief init_station_nodes Initializes StationNode structs for the graph
     * algorithms
     * \param station_nodes unordered_map conataining the StationNode structs
     */
    void init_station_nodes(std::unordered_map<StationID, StationNode> &station_nodes) {
        station_nodes.reserve(all_stations_map.size());
        for (auto& station : all_stations_map) {
            StationNode new_node = {station.second.station_id, station.second.coord,
                                    station.second.next_stations, station.second.departure_times};
            station_nodes.insert({station.first, new_node});
        }
    }

    /*!
     * \brief dijkstra Graph path finding algorithm based on Dijkstras algorithm
     * \param station is the StationID of the starting station
     * \param endStation is the StationID of the goal station
     * \param path is a vector containing the path from the starting station to
     * the end station
     * \param cost_func iis the ceost function for calculating the cost between
     * stations
     * \return returns true if a path was found or false if no path was found.
     */
    template<typename T>
    bool dijkstra(StationID station, StationID endStation, int starting_cost,
                  T& path, std::function<float(StationNode, StationNode)> cost_func) {


        if (station == endStation) {
            return true;
        }

        // Set everything to white and distances to -1
        std::unordered_map<StationID, StationNode> station_nodes;
        init_station_nodes(station_nodes);

        // Dijkstra
        auto comp = [](StationNode a, StationNode b) {return a.cost > b.cost;};
        std::priority_queue<StationNode, std::vector<StationNode>, decltype(comp)> Q(comp);

        station_nodes.at(station).color = 'g';
        station_nodes.at(station).cost = starting_cost;

        Q.push(station_nodes.at(station));
        while(!Q.empty()) {
            auto u = Q.top();
            // goal
            if (u.station_id == endStation) {
                path.push_back({u.station_id, u.cost});
                StationNode pi = station_nodes.at(u.prev);
                while (pi.station_id != station) {
                    path.push_back({pi.station_id, pi.cost});
                    pi = station_nodes.at(pi.prev);
                }
                path.push_back({pi.station_id, pi.cost});
                path.shrink_to_fit();
                std::reverse(path.begin(), path.end());
                //station_nodes.clear();
                return true;
            }

            for (auto& next_station : u.next_stations) {
                auto& v = station_nodes.at(next_station);

                // Relax
                bool cheaper = false;
                // calculate cost between nodes
                float cost = cost_func(u, v);

                if (v.cost == -1  || v.cost > u.cost + cost) {
                    v.cost = u.cost + cost;
                    v.prev = u.station_id;
                    cheaper = true;
                }

                // After relax
                if (v.color == 'w') {
                    v.color = 'g';
                    Q.push(v);
                } else {
                    if (cheaper) {
                        Q.push(v);
                    }
                }
            }
            u.color = 'b';
            Q.pop();
        }
        station_nodes.clear();
        return false;
    }
};

#endif // DATASTRUCTURES_HH

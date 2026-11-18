// Priority Queues in C++
// By default, it is a max-heap, meaning the largest element is at the top.

#include <cstdio>
#include <queue>

using namespace std;

int main() {

    // Implementing a max-heap priority queue
    priority_queue<int> pq;
    pq.push(10);
    pq.push(5);
    pq.push(20);

    printf("The largest element is: %d\n", pq.top()); // Outputs 20
    pq.pop(); // Removes the largest element (20)

    printf("The largest element after pop is: %d\n", pq.top()); // Outputs 10


    // Implementing a min-heap priority queue
    priority_queue<int, vector<int>, greater<int>> min_pq;
    min_pq.push(10);
    min_pq.push(5);
    min_pq.push(20);

    printf("The smallest element is: %d\n", min_pq.top()); // Outputs 5
    min_pq.pop(); // Removes the smallest element (5)

    printf("The smallest element after pop is: %d\n", min_pq.top()); // Outputs 10

    // Implementing a priority queue of pairs
    priority_queue<pair<int, int>> pq;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> min_pq;
    pq.push({10, 1});
    pq.push({20, 2});
    pq.push({20, 5});
}

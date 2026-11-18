// Lower and Upper bounds in C++

#include <cstdio>

using namespace std;

int main() {
    multiset<int> tickets = {5, 10, 15, 20, 25};

    auto it = tickets.upper_bound(18);
    if (it != tickets.begin()) {
        --it; // Move iterator to the largest ticket price less than or equal to 18
        printf("The largest ticket price less than or equal to 18 is: %d\n", *it);
    } else {
        printf("There is no ticket price less than or equal to 18.\n");
    }

    // For sequential containers like vectors follow the below process
    // Below example demonstrates finding an element in a sorted vector using lower_bound
    vector<int> ticketPrices = {5, 10, 15, 20, 25};
    auto it2 = lower_bound(ticketPrices.begin(), ticketPrices.end(), 15);

    if (it2 != ticketPrices.end() && *it2 == 15) {
        cout << "Found ticket price: " << *it2 << endl;
    } else {
        cout << "Ticket price not found." << endl;
    }

    // Ranges using lower_bound and upper_bound
    auto lower = lower_bound(ticketPrices.begin(), ticketPrices.end(), 10);
    auto upper = upper_bound(ticketPrices.begin(), ticketPrices.end(), 20);

    // Finding number of elements in the range [10, 20]
    int count = upper - lower;
    printf("Number of ticket prices in the range [10, 20]: %d\n", count);


    return 0;
}

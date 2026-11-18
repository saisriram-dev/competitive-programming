// To find the larget ticket price that is less than or equal to 18, 
// we can use the upper_bound function of the multiset. 
// The upper_bound function returns an iterator pointing to the first element that is greater than 
// the specified value. Therefore, we can decrement the iterator to get the largest ticket price 
// that is less than or equal to 18.

#include <cstdio>

int main() {
    multiset<int> tickets = {5, 10, 15, 20, 25};

    auto it = tickets.upper_bound(18);

    if (it == tickets.begin()){
        cout << -1 << '\n';
    } else {
        --it;
        cout << *it << '\n';
        tickets.erase(it);
    }
}

/*
TIME COMPLEXITIES OF VARIOUS OPERATIONS IN MULTISET:

1. insert(value): O(log n) - Inserts a new element into the multiset.
2. erase(value): O(log n + k) - where k occurrences of the value being erased.
3. find(value): O(log n) - Searches for an element in the multiset.
4. count(value): O(log n + k) - Counts the number of occurrences of a specific value.
5. erase(iterator): Amortized O(1) - Removes the element pointed to by the iterator.
*/

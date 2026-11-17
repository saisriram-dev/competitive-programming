#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// Helper function to print all elements of a vector separated by spaces.
// Passed by const reference to avoid unnecessary copying.
void printVector(const vector<ll>& v) {
    for (ll x : v) {
        cout << x << " ";
    }
    cout << '\n';
}

void solve() {
    
    // 1. DYNAMIC ARRAYS (std::vector) - Creation, Sizing, and Element Access
    int n;
    cin >> n;

    // Declare a vector of size 'n' initialized with default values (0)
    vector<ll> v(n);

    // Read elements into the vector using standard indexing
    for (int i = 0; i < n; i++) {
        cin >> v[i];
    }

    // Print vector elements using a range-based for loop
    for (ll x : v) {
        cout << x << " ";
    }
    cout << '\n';

    // Safe bounds-aware element access (ensure vector is not empty first)
    if (!v.empty()) {
        cout << v[0] << '\n';       // Access via standard operator[] (no bounds checking)
        cout << v.front() << '\n';  // Safe access to the first element
        cout << v.back() << '\n';   // Safe access to the last element
        cout << v.size() << '\n';   // Returns the number of elements (size_t)
    }

    // Check if the vector contains no elements
    cout << v.empty() << '\n';      // Returns 1 (true) if empty, 0 (false) otherwise


    // 2. VECTOR MODIFICATIONS - Insertion, Deletion, and Erase-Remove Idiom

    vector<ll> a = v; // Copy vector 'v' into 'a'

    a.push_back(100);       // Appends 100 to the end (copies or moves)
    a.emplace_back(200);    // Constructs 200 directly at the end (more efficient for objects)

    printVector(a);

    a.pop_back();           // Removes the very last element from the vector

    // Insert 50 at the very beginning (takes O(N) time as elements shift right)
    a.insert(a.begin(), 50);

    // Insert 75 at index 1 (between the first and second element)
    a.insert(a.begin() + 1, 75);

    // Erase the element specifically at index 1 (takes O(N) time)
    if (a.size() > 1) {
        a.erase(a.begin() + 1);
    }

    // "Erase-Remove Idiom": 
    // remove() moves all matching elements to the end and returns an iterator to the new logical end.
    // erase() then physically deletes them from that iterator to a.end().
    a.erase(remove(a.begin(), a.end(), 100), a.end());

    printVector(a);


    // 3. RANGE-BASED FOR LOOPS - Copies vs. References

    // Read-only traversal using copies (creates a temporary copy of each element)
    for (ll x : v) {
        cout << x << " ";
    }
    cout << '\n';

    // Modifying original elements using references (&)
    vector<ll> doubled = v;
    for (ll &x : doubled) {
        x *= 2; // Directly modifies elements inside the 'doubled' vector
    }
    printVector(doubled);

    // Read-only traversal without copying (best practice for large objects/structs)
    for (const ll &x : v) {
        cout << x << " ";
    }
    cout << '\n';


    // 4. ALGORITHMIC UTILITIES - Sum, Extrema, and Product

    // accumulate(start, end, initial_value) sums elements. 
    // 0LL specifies a long long initial value to prevent integer overflow.
    ll sum = accumulate(v.begin(), v.end(), 0LL);
    cout << sum << '\n';

    if (!v.empty()) {
        // min_element and max_element return iterators pointing to min/max values
        cout << *min_element(v.begin(), v.end()) << '\n';
        cout << *max_element(v.begin(), v.end()) << '\n';
    }

    // Calculating product manually (beware of potential overflow with large numbers)
    ll product = 1;
    for (ll x : v) {
        product *= x;
    }
    cout << product << '\n';


    // 5. SORTING AND REVERSING - Rearranging Data

    vector<ll> b = v;

    // Sort in ascending order (default behavior, O(N log N))
    sort(b.begin(), b.end());
    printVector(b);

    // Sort in descending order using greater<ll>() comparator
    sort(b.begin(), b.end(), greater<ll>());
    printVector(b);

    // Reverse the current arrangement of elements in-place (O(N))
    reverse(b.begin(), b.end());
    printVector(b);


    // 6. SEARCHING AND COUNTING - Linear Scans

    ll target = 10;

    // Linear search: finds the first occurrence of 'target'
    auto it = find(v.begin(), v.end(), target);

    if (it != v.end()) {
        // Pointer arithmetic: subtracting v.begin() gives the exact 0-based index
        cout << "Found at index: " << it - v.begin() << '\n';
    } else {
        cout << "Not found\n";
    }

    // Count how many times 'target' appears in the vector (O(N))
    cout << count(v.begin(), v.end(), target) << '\n';


    // 7. BINARY SEARCH - O(log N) Queries on Sorted Data

    vector<ll> sorted = v;
    sort(sorted.begin(), sorted.end()); // Binary search REQUIRES sorted data!

    // Check if target exists (returns true/false)
    bool exists = binary_search(sorted.begin(), sorted.end(), target);
    cout << exists << '\n';

    // lower_bound: Returns iterator to the first element >= target
    auto lb = lower_bound(sorted.begin(), sorted.end(), target);

    // upper_bound: Returns iterator to the first element strictly > target
    auto ub = upper_bound(sorted.begin(), sorted.end(), target);

    // Convert iterators to indices
    cout << lb - sorted.begin() << '\n';
    cout << ub - sorted.begin() << '\n';


    // 8. STRINGS - Dynamic Character Arrays

    string s;
    cin >> s;

    cout << s << '\n';
    cout << s.size() << '\n';
    cout << s[0] << '\n';
    cout << s.front() << '\n';
    cout << s.back() << '\n';

    s.push_back('x');   // Append character 'x' to the end of the string
    s.pop_back();       // Remove the last character

    // Extract substring starting at index 0 with length 3
    cout << s.substr(0, 3) << '\n';

    // Find the starting index of a substring (returns string::npos if not found)
    cout << s.find("abc") << '\n';

    // Sort characters alphabetically
    string sortedString = s;
    sort(sortedString.begin(), sortedString.end());
    cout << sortedString << '\n';

    // Reverse the string in-place
    reverse(s.begin(), s.end());
    cout << s << '\n';


    // 9. PAIRS AND CUSTOM SORTING - Grouping Data & Lambdas

    pair<ll, ll> p = {10, 20};
    cout << p.first << " " << p.second << '\n';

    int m;
    cin >> m;

    vector<pair<ll, ll>> vp(m);

    // Read pairs into vector
    for (auto &pr : vp) {
        cin >> pr.first >> pr.second;
    }

    // Default sorting for pairs: 
    // Compares 'first' elements first. If they are equal, compares 'second' elements.
    sort(vp.begin(), vp.end());

    for (auto pr : vp) {
        cout << pr.first << " " << pr.second << '\n';
    }

    // Custom sorting using a Lambda expression:
    // Sort primarily by 'second' value (ascending), and secondarily by 'first' value (ascending).
    sort(vp.begin(), vp.end(), [](const auto &x, const auto &y) {
        if (x.second != y.second) {
            return x.second < y.second;
        }
        return x.first < y.first;
    });

    // Structured binding (C++17) to unpack pairs easily in a loop
    for (auto [x, y] : vp) {
        cout << x << " " << y << '\n';
    }
}

int main() {
    // Optimizes standard I/O operations for competitive programming speed
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t; // Read number of test cases

    while (t--) {
        solve(); // Run solve function for each test case
    }

    return 0;
}

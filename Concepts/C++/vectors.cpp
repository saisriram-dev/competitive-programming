#include <cstudio>

int main() {
    vector<int> a = {1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7}

    map<int, int> freq;

    for (int num: a) {
        freq[num]++;
    }

    for (auto [key, value]: freq) {
        cout << key << " -> " << value << '\n';
    }

    
    vector<int> b = {1, 1, 2, 3, 3, 4, 5, 6, 7, 7, 7};

    unordered_map<int, int> freq_unordered;

    for (int num: b) {
        freq_unordered[num]++;
    }
    
    for (auto [key, value]: freq_unordered) {
        cout << key << " -> " << value << '\n';
    }

}

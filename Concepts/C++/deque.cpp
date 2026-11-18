// Deque: Inserting and removing elements from both ends of a sequence container

#include <cstdio>
#include <deque>

using namespace std;

int main() {
    deque<int> dq;
    dq.push_back(1);
    dq.push_back(2);
    dq.push_front(0);
    dq.push_front(-1);

    printf("Deque elements: ");
    for (int val: dq) {
        printf("%d ", val);
    }

    dq.pop_front()
    dq.pop_back()
}

#include "tools.hpp"
// ====== 函数定义 ======
void printVector(const std::vector<int> data)
{
    for (int n : data)
    {
        std::cout << n << " ";
    }
    std::cout << std::endl;
}

#include <iostream>
#include <vector>
#include "tools.hpp"

// ====== 函数声明 ======
// 功能：输出 vector 中的所有元素
// void printVector(const std::vector<int> data);

int main()
{
    // 1. 基本变量类型
    int age = 20;           // 整数类型
    double pi = 3.14159;    // 浮点型
    char grade = 'A';       // 字符型
    bool is_student = true; // 布尔型

    std::cout << "Age: " << age << std::endl;
    std::cout << "Pi: " << pi << std::endl;
    std::cout << "Grade: " << grade << std::endl;
    std::cout << "Is student: " << is_student << std::endl;

    // 2. 定义一个整数数组（vector）
    std::vector<int> numbers = {12, 45, 200, 180, 255, 90, 30};

    // 3. 条件判断 if
    // 模拟二值化：大于128 → 1，否则 → 0
    std::vector<int> binary;
    for (int n : numbers)
    {
        if (n > 128)
            binary.push_back(1);
        else
            binary.push_back(0);
    }
    // 4. 调用函数打印
    std::cout << "Numbers: ";
    printVector(numbers);
    std::cout << "Binary: ";
    printVector(binary);

    return 0;
}

// ====== 函数定义 ======
// void printVector(const std::vector<int> data)
// {
//     for (int n : data)
//     {
//         std::cout << n << " ";
//     }
//     std::cout << std::endl;
// }

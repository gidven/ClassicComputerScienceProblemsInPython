# fib1.py
# From Classic Computer Science Problems in Python Chapter 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


#  Using flake8 linting with flake8-mypy to enable type checking

def fib1(n: int) -> int:

    # missing base case causes infinite recursion

    return fib1(n - 1) + fib1(n - 2)


# this function is a more efficient approach
def fib_new(n: int, result: int = 0) -> int:
    if n < 1:  # base case
        return result
    else:
        return fib_new(n-1, result+n)


if __name__ == "__main__":

    # uncomment any of the below lines to test these cases

    # print(fib1(5))  # this results in max recursion depth

    print(fib_new(512))  # this version is more efficient

    # print(fib_new(100.1))  # flake8-mypy correctly identifies type conflict

    print(fib_new(800))  # this works fine

    # print(fib_new(1000))  # although it has its limits

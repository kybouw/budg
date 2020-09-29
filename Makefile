CXX := g++
CXX_FLAGS := -Wall -Wextra -std=c++17 -ggdb

.PHONY: default clean

default: budg

clean:
	rm budg
	rm -r objs

budg: objs/budg.o
	$(CXX) $(CXX_FLAGS) -o budg objs/budg.o

objs/budg.o: src/budg.cpp src/budg.hpp objs
	$(CXX) $(CXX_FLAGS) -c -o objs/budg.o src/budg.cpp

objs:
	mkdir objs

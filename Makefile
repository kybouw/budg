CXX := g++
CXX_FLAGS := -Wall -Wextra -std=c++17 -ggdb

.PHONY: default clean

default: budg

clean:
	rm budg
	rm -r objs

budg: objs/budg.o objs/plan.o objs/lineitem.o
	$(CXX) $(CXX_FLAGS) -o budg objs/budg.o objs/plan.o objs/lineitem.o

objs/budg.o: src/budg.cpp src/budg.hpp src/plan.hpp src/lineitem.hpp objs
	$(CXX) $(CXX_FLAGS) -c -o objs/budg.o src/budg.cpp

objs/plan.o: src/plan.cpp src/plan.hpp src/lineitem.hpp objs
	$(CXX) $(CXX_FLAGS) -c -o objs/plan.o src/plan.cpp

objs/lineitem.o: src/lineitem.cpp src/lineitem.hpp objs
	$(CXX) $(CXX_FLAGS) -c -o objs/lineitem.o src/lineitem.cpp

objs:
	mkdir objs

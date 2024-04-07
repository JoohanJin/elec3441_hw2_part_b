# Makefile to generate riscv binaries


CC=riscv32-unknown-elf-gcc
CXX=riscv32-unknown-elf-g++

benchmarks=\
	bfs_matrix \
	bfs_pointer \
	conv2D  \
	kmean   \
	mm      \
	sobel   \
	fir     \
	quicksort \

all :
	-for d in $(benchmarks); do ($(MAKE) -C $$d) ; done

run :
	-for d in $(benchmarks); do (cd $$d && spike pk $$d && cd ..) ; done

clean:
	-for d in $(benchmarks); do ($(MAKE) -C $$d clean) ; done

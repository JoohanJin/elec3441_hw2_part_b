CC = riscv32-unknown-elf-gcc
#CFLAGS= -DDEBUG -g -Wall
CFLAGS= -g -O3 
TARGET = conv2D 
SRCS = conv2D.c 


OBJS = $(SRCS:.c=.o)

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $@ 2>&1 | c++filt

.cpp.o:
	$(CC) -c $(CFLAGS) $< -o  $@

clean:
	rm -f $(OBJS) $(TARGET) core.*

depend:
	makedepend $(SRCS)

# DO NOT DELETE



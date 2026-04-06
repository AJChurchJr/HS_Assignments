# Compiler and flags
CC = D:\mingw64\bin\g++.exe

CFLAGS = -Wall --static

# Source files
SRCS := $(wildcard *.cpp)

# Object files
OBJS = $(SRCS:.c=.o)

# Executable
EXEC = main

# Default target
all: $(EXEC)

# Compile source files into object files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Link object files into the executable
$(EXEC): $(OBJS)
	$(CC) $(CFLAGS) $^ -o $@

# Clean up object files and executable
clean:
	rm -f $(OBJS) $(EXEC)
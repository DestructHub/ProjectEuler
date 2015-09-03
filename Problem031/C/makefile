GCC = gcc
LFLAGS = -lm -Wall -o
TARGET =  solution_1
DEBUG = --debug

all: 
	$(GCC) $(LFLAGS) $(TARGET).out $(TARGET).c
debug:
	$(GCC) $(DEBUG) $(LFLAGS) $(TARGET).out $(TARGET).c
clean: 
	rm -v *.out
run:
	./$(TARGET).out

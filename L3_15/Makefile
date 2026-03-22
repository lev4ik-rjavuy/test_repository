CXX = g++ 
CXXFLAGS = -std=c++17 -Wall -Wextra -O2 

TARGET = app 
SOURCES = main.cpp Currency.cpp Converter.cpp 
OBJECTS = $(SOURCES:.cpp=.o) 

all: $(TARGET) 

$(TARGET): $(OBJECTS) 
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $(TARGET) 

main.o: main.cpp Currency.h Converter.h
	$(CXX) $(CXXFLAGS) -c main.cpp -o main.o 

Property.o: Currency.cpp Currency.h 
	$(CXX) $(CXXFLAGS) -c Currency.cpp -o Currency.o 

Agency.o: Converter.cpp Converter.h Currency.h 
	$(CXX) $(CXXFLAGS) -c Converter.cpp -o Converter.o 

clean: 
	rm -f $(OBJECTS) $(TARGET) 

.PHONY: all clean 
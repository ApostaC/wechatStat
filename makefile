FLAGS = -std=c++14
TARGETS = analysisTime

all: analysisTime 

analysisTime: analysisTime.cpp 
	g++ analysisTime.cpp -o analysisTime ${FLAGS}

clean:
	rm -rf ${TARGETS}
	rm -rf *.o

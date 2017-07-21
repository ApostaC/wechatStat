#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;

class Time
{
public:
    int h,m,s;
    Time(int _h=0,int _m=0,int _s=0):h(_h),m(_m),s(_s){}

	friend ostream & operator<<(ostream & o,const Time & t)
	{
		o<<t.h<<":"<<t.m<<":"<<t.s;
		return o;
	}

    const Time & operator+=(const Time & t)
    {
        this->s+=t.s;
        if(this->s>=60) {this->s-=60;this->m++;}
        this->m+=t.m;
        if(this->m>=60) {this->m-=60;this->h++;}
        this->h+=t.h;
        if(this->h>=24) this->h-=24;
        return *this;
    }

	Time operator+(const Time & t)
	{
		Time t2=*this;
		t2+=t;
		return t2;
	}

	const Time & operator-=(const Time & t)
	{
		this->s-=t.s;
		if(this->s<0) {this->s+=60;this->m--;}
		this->m-=t.m;
		if(this->m<0) {this->m+=60;this->h--;}
		this->h-=t.h;
		if(this->h<0) this->h+=24;
		return *this;
	}

	Time operator-(const Time & t)
	{
		Time t2=*this;
		t2-=t;
		return t2;
	}

	bool operator==(const Time & t)
	{
		return this->s==t.s && this->m==t.m && this->h==t.h;
	}
	
	bool operator<(const Time & t)
	{
		if(this->h==t.h)
		{
			if(this->m==t.m)
				return this->s<t.s;
			return this->m<t.m;
		}
		return this->h<t.h;
	}

	bool operator>(const Time & t)
	{
		if(*this<t) return false;
		if(*this==t) return false;
		return true;
	}

	bool operator <=(const Time & t) {return *this>t || *this==t;}
	bool operator >=(const Time & t) {return !(*this<t);}
};

bool operator<(const Time & l,const Time & r)
{
	return l<r;
}

Time threeMin(0,3,0);
vector<Time> tt;
map<int,int> numPerHour;
map<Time,int> inThreeMin;

int main(int argc, char * argv[])
{
	if(argc!=3)
	{
		cerr<<"Usage: ./analysisTime <fileName> <output_prefix>"<<endl;
		exit(-1);
	}
	string prefix(argv[2]);
	fstream fin;
	fin.open(argv[1]);
	string ss;
	getline(fin,ss);
	int n,h,m,s;char c;string day;
	while(!fin.eof())
	{
		fin>>n>>c;
		fin>>day;
		fin>>h>>c>>m>>c>>s;
		tt.push_back(Time(h,m,s));
	}
	fin.close();
	for(Time t:tt)
		numPerHour[t.h]++;
	ofstream  fout;
	fout.open(prefix+"-numPerHour.csv");
	for(auto i:numPerHour)
		fout<<i.first<<","<<i.second<<endl;

	cout<<"written into "<<prefix+"-numPerHour.csv"<<endl;
	int maxt=0;Time maxTime;
	queue<Time> Q;
	for(Time t:tt)
	{
		Q.push(t);
		Time vv=t-Q.front();
		if(vv>threeMin)
		{
			Time temp=Q.front();
			Q.pop();
			if(Q.size()>maxt) 
			{
				maxt=Q.size();maxTime=temp;
			}
		}
	}


	cout<<maxTime<<" to "<<maxTime+threeMin<<" have "<<maxt<<endl;
	return 0;
}

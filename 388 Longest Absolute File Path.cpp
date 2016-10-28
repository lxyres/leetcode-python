class Solution {
public:
    int lengthLongestPath(string input) 
    {
        int result=0;
        vector<int> store(1);
        while (!input.empty())
        {
            int pos=input.find("\n");
            string tmp=input.substr(0,pos);
            if (pos==string::npos)
            {
                input="";
            }
            else
            {
                input=input.substr(pos+1);
            }
            int index=0;
            while ((pos=tmp.find("\t"))!=string::npos)
            {
                index+=1;
                tmp=tmp.substr(pos+1);
            }
            if (tmp.find(".")==string::npos)
            {
                if (index==0) store[0]=tmp.length()+1;
                else if (index>=store.size()) store.push_back(store.back()+tmp.length()+1);
                else store[index]=store[index-1]+tmp.length()+1;
            }
            else
            {
                if (index==0) result=max(result,(int)tmp.length());
                else result=max(result,(int)store[index-1]+(int)tmp.length());
            }
        }
        return result;
    }
};
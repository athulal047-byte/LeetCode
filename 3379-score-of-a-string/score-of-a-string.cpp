class Solution{
public:
    int scoreOfString(string s){
        int score =0;
        for (char &a : s){
            a=tolower(a);
        }
        for(int i=0;i<s.length()-1;i++){
            score += abs(s[i]- s[i+1]);
        }
        return score;
    }
};
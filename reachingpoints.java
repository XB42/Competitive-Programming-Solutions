class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        System.out.println(sx +" "+sy +" "+ tx +" "+ty);
        if (sx == tx && sy == ty) 
            return true;
        else if(sx> tx || sy>ty || tx == ty)
            return false;
        else{
            int n;
            if(tx<ty){
                n = (ty - sy)/tx;
                if(n==0) n=1;
                return reachingPoints(sx,sy,tx,ty-n*tx);
            }
            else{
                n = (tx - sx)/ty;
                if(n==0)n=1;
                return reachingPoints(sx,sy,tx-n*ty,ty);
            }
        }
    }
}

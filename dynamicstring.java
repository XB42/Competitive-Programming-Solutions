
import java.util.*;
public class dynamicstring
{
    static Scanner sc = new Scanner(System.in);
    char letter;
    int freq;
    dynamicstring( char letter, int freq)
    {
        this. letter = letter;
        this. freq = freq;
    
    }
    
    public static void dynamicstring(String args[])
    {
        
        int T= 0;
        int i,j,k,a,b,c;
        int n;
        char ch;
        int ctr = 0;
        boolean flag = false;
        if(sc.hasNextInt())
        T = sc.nextInt();
        else System.exit(0);
        if(T<=10){
        String S[] = new String[T];
            for(n = 1; n<=T ; n ++)
        {
            if(sc.hasNext())
        S[n-1] = sc.next();
        else System.exit(0);
            
        }
            
            
        for(n = 0; n<T ; n ++)
        {
            dynamicstring fb[] = new dynamicstring[S[n].length()];
            for( i = 0; i < S[n].length(); i ++)
            {
                   fb[i] = new px[i]('0',0);
                }
            flag = false;
            ctr = 0;
            for( i = 0; i< S[n].length(); i++)
            {
                
                ch = S[n].charAt(i);
                if(S[n].indexOf(ch)== i)
                {
                    fb[ctr].letter = ch;
                    fb[ctr++].freq = 1;
                    
                }
                else
                {
                    for( j = 0; j<= i; j++)
                    {
                        if(fb[j].letter == ch)
                        {
                            fb[j].freq++;
                            break;
                        }
                    
                    }
               }
            }
            for( i = 0; i < fb.length; i ++)
               {
                   if(fb[i].freq == 0)break;
                    a = fb[i].freq;
                   for( j = 0; j < fb.length; j ++)
                  {
                      if(i ==j) break;
                     if(fb[j].freq == 0)break;
                      b = fb[j].freq;
                     for( k = 0; k < fb.length; k ++)
                     {
                         if(k ==j) break;
                       if(fb[k].freq == 0)break;
                        c = fb[k].freq;
                       if(a == b+c || b==a+c || c == a+b)
                       {
                           flag = true;
                           break;
                        }
                    }
                    if(flag)break;
                  }
                   if(flag)break;
              }   
                if(flag)System.out.println("Dynamic");
                else System.out.println("Not");
                
       }//end of test case
       }
       System.exit(0);
    
    }
}

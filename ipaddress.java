class Solution {
    public String defangIPaddr(String address) {
        String na = "";
        char ch;
        
        for(int i = 0; i<address.length(); i++){
            ch = address.charAt(i);
            if(ch == '.'){
                na += "[.]";
            }
            else{
                na += ch;
                
            }
        
        }
        return na;
    }
}
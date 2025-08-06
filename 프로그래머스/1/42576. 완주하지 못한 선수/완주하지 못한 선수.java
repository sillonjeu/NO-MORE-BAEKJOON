import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();
        
        for (int i = 0; i < participant.length; i++) {
            map.putIfAbsent(participant[i], 0);
            map.put(participant[i], map.get(participant[i]) + 1);
                
        }
        
        for (int i = 0; i < completion.length; i++) {
            map.put(completion[i], map.get(completion[i]) - 1);
        }
        
        String[] keys = map.keySet().toArray(new String[map.size()]);
        
        for (int i = 0; i < keys.length; i++) {
            if (map.get(keys[i]) == 1) {
                return keys[i];
            }
        }
        
        return null;
    }
}
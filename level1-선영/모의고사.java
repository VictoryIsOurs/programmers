import java.util.ArrayList;


class Solution {
    public int[] solution(int[] answers) {
        int[] answer = {};
        
        int[] user1 = {1, 2, 3, 4, 5};
        int[] user2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] user3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int[] user_sol = {0, 0, 0};
        
        for(int i = 0; i < answers.length; i++){
            if(answers[i%5] == user1[i]){
                user_sol[0]++;
            }if(answers[i%8] == user2[i]){
                user_sol[1]++;
            }if(answers[i%10] == user3[i]){
                user_sol[2]++;
            }
        }
        
        int max_score = Math.max(Math.max(user_sol[0], user_sol[1]), user_sol[2]);
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        if(max_score == user_sol[0]) list.add(1);
        if(max_score == user_sol[1]) list.add(2);
        if(max_score == user_sol[2]) list.add(3);
        
        answer = new int[ list.size()];
        for( int i=0; i<list.size(); i++){
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}

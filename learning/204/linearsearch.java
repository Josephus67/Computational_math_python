public class linearsearch{
    
    public static void main(String [] args){
        int[] array={3,2,1,4,3,6,75,54};
        int target=632;
        for (int i=0; i<array.length; i++){
            if (target==array[i]){
                System.out.println(target+" is found in the array");
            }
           }
    }
}
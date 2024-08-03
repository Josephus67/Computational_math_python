public class findMax {
    public static void main(String[] args){
        int[] array={39,3,5,22,34,89,99,33,23};
        int max=array[0];
        for (int i=1; i<array.length; i++){
            if (max<array[i]){
                max=array[i];
            }
        }
        System.out.println("The maximum number in the array is: "+max);  // Print the maximum number in the array.
    }
}

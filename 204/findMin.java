    public class findMin {
    
        public static void  main(String[] args){
            int[] array={33,3,45,6,7,8,3,4,7,74};
            int min=array[0];
            for(int i=1; i<array.length;i++){
                if (min>array[i]){
                    min=array[i];
                }
            }
            System.out.println(min+" is the minimum value of the given array");
        }
    }
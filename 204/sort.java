public class sort {
   public static void main(String[] args){
         int[] array={3,2,1,4,3,6,75,54};
         for (int i=0; i<array.length; i++){
              for (int j=i+1; j<array.length; j++){
                if (array[i]>array[j]){
                     int temp=array[i];
                     array[i]=array[j];
                     array[j]=temp;
                }
              }
         }
         for (int i=0; i<array.length; i++){
              System.out.print(array[i]+" ");
         }
   } 
}

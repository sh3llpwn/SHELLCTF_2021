import java.security.MessageDigest;

class Crack{
    private static void displayHash(byte[] digest){
      StringBuffer hexString = new StringBuffer();
      for (int i = 0;i<digest.length;i++) {
         hexString.append(Integer.toHexString(0xFF & digest[i]));
      }
      System.out.println("Hash : " + hexString.toString());
    }

    private static byte[] sha256sum(byte[] inputBytes) throws Exception{
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(inputBytes);
        byte[] digest = md.digest();
        return digest;
    }

    private static byte[] hashIter(byte[] input,int iterations)throws Exception{
        byte[] output = input;
        for(int i=0;i<iterations;i++){
            output = sha256sum(output);
        }
        return output;
    }

    public static void main(String args[])throws Exception{
        System.out.println("Initialized ");
        String initialString = "awesome_secure_password";
        byte[] output = hashIter(initialString.getBytes(), 0xFFFFFFF);
        displayHash(output);
    }
}
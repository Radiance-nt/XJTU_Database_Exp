import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.util.concurrent.TimeUnit;

public class DBTest {
    public static Connection GetConnection(String username, String passwd, String db, Integer port) {
        String driver = "org.postgresql.Driver";
        String sourceURL = String.format("jdbc:postgresql://localhost:%d/%s", port, db);
        Connection conn;
        try {

            Class.forName(driver);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }

        try {
            //创建数据库连接。
            conn = DriverManager.getConnection(sourceURL, username, passwd);
            System.out.println("Connection succeed!");
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }

        return conn;
    }
    public static void ExecCommand(Connection conn, String command) throws InterruptedException {
        Statement stmt = null;
        try {
            stmt = conn.createStatement();

            stmt.execute(command);

            stmt.close();
            TimeUnit.MICROSECONDS.sleep(1000);

        } catch (SQLException e) {
            System.out.println("Error occurs when executing " + command);

            if (stmt != null) {
                try {
                    stmt.close();
                } catch (SQLException e1) {
                    e1.printStackTrace();
                }
            }
            e.printStackTrace();
        }
    }

    public static void ExecSelect(Connection conn, String sql) {

        Statement stmt =null;
        try {
            stmt = conn.createStatement();
            System.out.println("=======================================");
            System.out.printf("Executing %s:%n",sql);
            ResultSet rs = stmt.executeQuery(sql);
            String str=null;
            while(rs.next()){
                str = "";
                for(int i=1;i<=rs.getMetaData().getColumnCount();i++){
                    str += rs.getString(i)+",";
                }
                System.out.println(str);
            }
            if (str == null){
                System.out.println("Found empty!");
            }
            System.out.println("=======================================");
            rs.close();
            stmt.close();
        } catch (SQLException e) {
            if (stmt != null) {
                try {
                    stmt.close();
                }
                catch (SQLException e1) {
                    e1.printStackTrace();
                }
            }
            System.out.println("Error!");
            e.printStackTrace();
            System.out.println("=======================================");

        }
    }
    public static void ExecFile(Connection conn, String filename) throws IOException, InterruptedException {

        FileReader fr=new FileReader(filename);
        BufferedReader br=new BufferedReader(fr);
        String line;
        String buf="";

        while ((line=br.readLine())!=null) {
            if (!line.contains("--")){
                buf = buf + line + " ";
            }
            if (line.contains(";")){
                if (buf.toLowerCase().contains("select") & !buf.toLowerCase().contains("create")){
                    ExecSelect(conn, buf);
                }
                else {
                    System.out.println(buf);
                    ExecCommand(conn, buf);
                }
                buf = "";
            }
        }
        br.close();
        fr.close();

    }
    /**
     * 主程序
     */
    public static void main(String[] args){
        //创建数据库连接。
        String USERNAME = "radiance";
        String PASSWORD = "Sql123456";
        String DB = "exp";
        Integer PORT = 5432;
        try {
            Connection conn = GetConnection(USERNAME, PASSWORD, DB, PORT);
            assert conn != null;

            ExecFile(conn, "./script/drop");

            ExecFile(conn, "./script/create");

            ExecFile(conn, "./script/insert");

            ExecFile(conn, "./script/expand");

            ExecFile(conn, "./script/select");
//
            ExecFile(conn, "./script/update");

            ExecFile(conn, "./script/drop");

            conn.close();

        } catch (SQLException e) {
            e.printStackTrace();
        } catch (IOException | InterruptedException e) {
            throw new RuntimeException(e);
        }
    }
}

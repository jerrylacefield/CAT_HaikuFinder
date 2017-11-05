package manager;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.concurrent.atomic.AtomicLong;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;



@RestController
public class LinkController {

    private static final String TEMPLATE = "%s";
    private final AtomicLong counter = new AtomicLong();

    @RequestMapping("/getLink")
    public Request getLink(@RequestParam(value="type", defaultValue="") String type) {
        String link = getLinkFromDB( Integer.parseInt(type));
        String []data = {"",""};
        return new Request(counter.incrementAndGet(), link, Integer.parseInt(type), data);
    }
    
    @RequestMapping("/updateData")
    public Request updateData(@RequestParam(value="link", defaultValue="") String link,
                            @RequestParam(value="type", defaultValue="") String type,
                            @RequestParam(value="data[]", defaultValue="") String[] data) {
        
        Request r =  new Request(counter.incrementAndGet(), link, Integer.parseInt(type), data);
        insertIntoDB(r);
        return r;
    }
    
    String getLinkFromDB(int type){
        try {
            System.out.println("In Get Link From DB");
            Connection con = setupConnection();
            PreparedStatement ps = null;
            String updateSQL = null;
            String linkType = null;
            System.out.println("In Get Link From DB2");
            switch(type){
                case 0:
                    ps = con.prepareCall("SELECT group_link FROM Groups WHERE NOT curr_working AND NOT is_done");
                    updateSQL = "UPDATE Groups SET curr_working = TRUE WHERE group_link = ?";
                    linkType = "group_link";
                    break;
                case 1:
                    ps = con.prepareCall("SELECT artist_link FROM Artists WHERE NOT curr_working AND NOT is_done");
                    updateSQL = "UPDATE Artists SET curr_working = TRUE WHERE artist_link = ?";
                    linkType = "artist_link";
                    break;
                case 2:
                    ps = con.prepareCall("SELECT song_link FROM Songs WHERE NOT curr_working AND NOT is_done");
                    updateSQL = "UPDATE Songs SET curr_working = TRUE WHERE song_link = ?";
                    linkType = "song_link";
                    break;
            }
            System.out.println("In Get Link From DB3");
            if(ps != null){
                ResultSet rs = ps.executeQuery();
                String link = "";
                while(rs.next()){
                    link = rs.getString(linkType);
                }
                System.out.println("In Get Link From DB4");
                
                PreparedStatement updatePS = con.prepareCall(updateSQL);
                updatePS.setString(1, link);
                updatePS.executeUpdate();
                System.out.println("In Get Link From DB5");
                if(link != null && !link.equalsIgnoreCase("NULL")){
                    return link;
                }
                return "";
            }
            System.out.println("In Get Link From DB7");
            return null;
            
        } catch (SQLException ex) {
            Logger.getLogger(LinkController.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
    
    
    Connection setupConnection() throws SQLException{
        try {
            Class.forName("com.mysql.jdbc.Driver");
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(LinkController.class.getName()).log(Level.SEVERE, null, ex);
        }
        return DriverManager.getConnection("jdbc:mysql://35.202.215.144:3306/lyrical_haikus", "root", "constantAlpha");
        
    }
    
    void insertIntoDB(Request r){
        try {
            Connection con = setupConnection();
            
            PreparedStatement ps = prepareStatement(r, con);
            
            ps.executeUpdate();
            con.close();
        } catch ( SQLException e) {
            System.out.println(e);
        }
    }
    
    PreparedStatement prepareStatement(Request r, Connection con) throws SQLException{
        PreparedStatement ps = null;
        String sql;
        switch(r.getType()){
            case 0:
                sql = "INSERT INTO Artists (artist_link, artist_name, curr_working, is_done) VALUES (?, ?, FALSE, FALSE)";
                ps = con.prepareStatement(sql);
                ps.setString(1, r.getLink());
                ps.setString(2, r.getData()[0]);
                break;
            case 1:
                sql = "INSERT INTO Songs (song_link, song_name, curr_working, is_done) VALUES (?, ?, FALSE, FALSE)";
                ps = con.prepareStatement(sql);
               // ps.setString(1, r.getLink());
                ps.setString(1, r.getLink());
                ps.setString(2, r.getData()[0]);
                ps.setString(3, r.getData()[1]);

                break;
            case 2:
                sql = "UPDATE Songs SET song_lyrics = ? WHERE song_link = ?";
                ps = con.prepareStatement(sql);
                ps.setString(1, r.getData()[0]);
                ps.setString(2, r.getLink());
                break;
        }
        return ps;
    }
}

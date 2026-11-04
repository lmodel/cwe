package example;

/* metamodel_version: 1.12.0 */
/* version: 5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A remark on an entry that fits nowhere else.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweNote  {

  private String type;
  private String version;
  private LocalDate releaseDate;
  private String value;


}
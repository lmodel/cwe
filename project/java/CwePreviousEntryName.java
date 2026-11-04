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
  A name an entry had before.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CwePreviousEntryName  {

  private LocalDate date;
  private String version;
  private String value;


}
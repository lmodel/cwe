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
  Another name people use for a weakness.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweAlternateTerm  {

  private String term;
  private List<String> role;
  private String description;


}
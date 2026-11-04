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
  A block of code in a worked example.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweExampleCode  {

  private String nature;
  private String language;
  private String value;


}
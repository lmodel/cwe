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
  One thing that can follow when a weakness is exploited.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweConsequence  {

  private String consequenceID;
  private List<String> scope;
  private List<String> impact;
  private String likelihood;
  private String note;


}
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
  A weakness that may suit a mapping better than this entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweMappingSuggestion  {

  private CweWeakness cWEID;
  private String comment;


}
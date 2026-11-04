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
  One short label that sums up the usage of an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweMappingReason  {

  private String type;


}
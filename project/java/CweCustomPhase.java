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
  A life cycle stage from a field whose stages differ from those of software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweCustomPhase  {

  private String domain;
  private String value;


}
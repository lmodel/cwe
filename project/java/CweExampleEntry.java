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
  One step of a worked example, either some prose or some code.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweExampleEntry  {

  private String bodyText;
  private CweExampleCode exampleCode;


}
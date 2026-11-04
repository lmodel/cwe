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
  A worked example of how a weakness looks in code.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweDemonstrativeExample  {

  private String demonstrativeExampleID;
  private String titleText;
  private String introText;
  private List<CweExampleEntry> entries;


}
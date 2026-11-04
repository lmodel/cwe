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
  The record of who wrote an entry and how it has changed since.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweContentHistory  {

  private List<CweSubmission> submission;
  private List<CweModification> modification;
  private List<CweContribution> contribution;
  private List<CwePreviousEntryName> previousEntryName;


}
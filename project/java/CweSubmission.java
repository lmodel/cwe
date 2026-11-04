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
  Who first submitted an entry, and when it joined the list.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweSubmission  {

  private List<String> submissionName;
  private String submissionOrganization;
  private LocalDate submissionDate;
  private String submissionVersion;
  private LocalDate submissionReleaseDate;
  private String submissionComment;


}
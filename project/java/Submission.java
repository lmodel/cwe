package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Initial submission record for a CWE entry (ContentHistoryType/Submission in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Submission  {

  private String submissionName;
  private String submissionOrganization;
  private LocalDate submissionDate;
  private String submissionVersion;
  private LocalDate submissionReleaseDate;
  private String submissionComment;

}
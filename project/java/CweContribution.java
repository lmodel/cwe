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
  Feedback or content that someone gave to an entry.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweContribution  {

  private String type;
  private List<String> contributionName;
  private String contributionOrganization;
  private LocalDate contributionDate;
  private String contributionVersion;
  private LocalDate contributionReleaseDate;
  private String contributionComment;


}
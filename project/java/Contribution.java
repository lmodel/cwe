package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A contribution record documenting donated content or feedback (ContentHistoryType/Contribution in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Contribution  {

  private String type;
  private String contributionName;
  private String contributionOrganization;
  private LocalDate contributionDate;
  private String contributionVersion;
  private LocalDate contributionReleaseDate;
  private String contributionComment;

}
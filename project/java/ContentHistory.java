package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Tracks the original author and subsequent modifications (ContentHistoryType in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ContentHistory  {

  private Submission submission;
  private List<Modification> modifications;
  private List<Contribution> contributions;
  private List<PreviousEntryName> previousEntryNames;

}
package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A modification record documenting a change to a CWE entry (ContentHistoryType/Modification in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Modification  {

  private String modificationName;
  private String modificationOrganization;
  private LocalDate modificationDate;
  private String modificationVersion;
  private LocalDate modificationReleaseDate;
  private String modificationImportance;
  private String modificationComment;

}
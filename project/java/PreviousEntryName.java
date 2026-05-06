package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A previous name used for a CWE entry before a substantive rename (ContentHistoryType/Previous_Entry_Name in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PreviousEntryName  {

  private String name;
  private LocalDate date;
  private String version;

}
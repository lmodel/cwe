package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Additional commentary about a CWE entry (NotesType/Note in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Note  {

  private String type;
  private String content;

}
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
  Any item of the CWE List that has an identifier of its own: a weakness, a grouping or a view.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class CweEntry  {

  private String iD;
  private String name;
  private String status;
  private List<CweReference> references;
  private CweMappingNotes mappingNotes;
  private List<CweNote> notes;
  private CweContentHistory contentHistory;


}
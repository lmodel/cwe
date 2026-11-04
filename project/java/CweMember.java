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
  A link from a grouping or a view to an entry it holds or belongs to, in one view.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweMember  {

  private CweEntry cWEID;
  private CweView viewID;
  private List<CweDimension> dimensions;


}
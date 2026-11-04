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
  The entries that a grouping or a view holds or belongs to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CweRelationships  {

  private List<CweMember> memberOf;
  private List<CweMember> hasMember;


}
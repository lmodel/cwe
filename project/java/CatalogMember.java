package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  A Has_Member or Member_Of entry specifying a CWE ID and the View ID in which the membership holds (MemberType in XSD).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CatalogMember  {

  private int cweId;
  private int viewId;

}
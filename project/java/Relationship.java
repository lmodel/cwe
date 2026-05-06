package None;

/* metamodel_version: 1.7.0 */
/* version: 7.3 */
import java.util.List;
import lombok.*;

/**
  Container for category membership relationships (RelationshipsType in XSD). Holds Has_Member and optionally Member_Of lists.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Relationship  {

  private List<CatalogMember> hasMember;
  private List<CatalogMember> memberOf;

}